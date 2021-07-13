# Contribution Guide

## Publishing A New Version

To cut a new version, follow these steps:

- create and merge final feature branch updating `CHANGELOG.md`
- tag final commit hash with `git tag <VERSION>`, e.g. `git tag 0.1.3`.
- publish to pypi with:
```
docker-compose run --rm app bash publish.sh
```
- push tag to github with `git push --tags`