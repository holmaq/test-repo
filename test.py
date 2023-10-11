from azure.monitor.opentelemetry import configure_azure_monitor
from logging import getLogger, INFO

configure_azure_monitor(
    connection_string="InstrumentationKey=a0655b3a-2f50-4cdf-b006-890b3d7fd100;IngestionEndpoint=https://norwayeast-0.in.applicationinsights.azure.com/;LiveEndpoint=https://norwayeast.livediagnostics.monitor.azure.com/",

)

logger = getLogger("__name__")

logger.setLevel("INFO")

logger.info("Information log message")