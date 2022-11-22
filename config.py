#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MS-APP-ID", "")
    APP_PASSWORD = os.environ.get("MS-APP-PASSWORD", "")
    LUIS_APP_ID = os.environ.get("LUIS-APP-ID", "54f4df2a-6524-461f-8eb2-7fa061eb7450")
    LUIS_API_KEY = os.environ.get("LUIS-API-KEY", "f910dac7fdbc43edae026ab1e2c0da60")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LUIS-API-HOST-NAME", "westeurope.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "APP-INSIGHT-INSTRUMENTATION-KEY", "e0b97576-9247-4b6f-98bf-72553006698d"
    )
