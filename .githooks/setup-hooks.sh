#!/bin/bash


pre-commit install --config .githooks/pre-commit-config.yaml
pre-commit autoupdate --config .githooks/pre-commit-config.yaml

ln -sf "$(pwd)/.githooks/pre-push" "$(pwd)/.git/hooks/pre-push"