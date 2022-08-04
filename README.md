[![CodeQL](https://github.com/nacifyas/followups-ms/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/nacifyas/followups-ms/actions/workflows/codeql-analysis.yml)
[![Build](https://github.com/nacifyas/followups-ms/actions/workflows/flake8_mypy_build.yml/badge.svg)](https://github.com/nacifyas/followups-ms/actions/workflows/flake8_mypy_build.yml)

Microservice corresponding to manager users relationship (like a social network).

Follow the correspondig steps at the [API Gateway Microservice](https://github.com/nacifyas/gateway-edm-demo/) to install and use.

The functionality of this MS is to exclusivly handle user's followsups and its CRUD related operations.

This MS uses redis as its primary graph database, and its event stream for events sourcing.
