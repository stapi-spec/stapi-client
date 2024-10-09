# stapi-client

A python library/CLI-tool for interfacing with a STAPI-server

This is a work in progress.

## installation

For now, install as editable:

```
    pip install -r requirements/requirements.txt
    pip install -e .
```

## development

Install additional packages for development and testing:

```
    pip install -r requirements/requirements-dev.txt
```

## testing

Verify code-style:

```
    black --check --verbose src tests
```

Check types:

```
    mypy src
```

Run unit tests:

```
    pytest
```
