# Development Guide

- [Adding new environment variables](#adding-new-environment-variables)
- [Static Assets](#static-assets)
- [CSS](#css)
- [Troubleshooting](#troubleshooting)

## Adding new environment variables
You'll have to add it in 4 different places for it to pass through to your app.
1. First add it to the template: [./tools/.env-sample](./tools/.env-sample)
2. Then add it to your actual [./.env](./.env)
3. Add it to the "app ENV vars" list within [./docker/django.Dockerfile](./docker/django.Dockerfile) and rebuild your container with `make build`.
4. Add it the `app.environment:` list within [./docker/docker-compose.yml](./docker/docker-compose.yml).
5. Add it to your hosting service secrets. TBD

## Static Assets

If you have images, js, css, or other static assets that logically belong to the root project rather than a particular app, they should be placed into `base/static/base`. Otherwise, place them within their appropriate app.

If there are any necessary compiled static assets for local development (such as compiled tailwindcss), they should be outputted to `build/static/`. No content in the `build/` directory should be git commited, other than the base file structure. User uploaded media files should live in `build/media/`.

## CSS

This project uses [tailwind](https://tailwindcss.com/) to handle css styling.

If you want to create your own css files in addition to what tailwind provides, you can import them into the main.css entrypoint file:
`base/static/base/css/main.css`. See the tailwind [documentation](https://tailwindcss.com/docs/using-with-preprocessors#build-time-imports) if you have more questions about importing css files.

## Troubleshooting

We have a couple of Makefile commands that can help with troubleshooting.

- `make shell_plus` lets you shell into a running django app container if you want to manually run any Python code within your django app or investigate your data.
- `make db-shell` will let you read the raw data within your postgres database. I don't recommend writing, updating, or deleting any data outside of the django `make shell_plus` console unless you know what you're doing.
- `make troubleshoot` will start a django app docker container without starting the django app server. There may be some cases where you need to troubleshoot the construction of the Docker container itself and not a bug within your Python code. This option can allow you to `make shell` into a container to investigate what may be going wrong with your system.