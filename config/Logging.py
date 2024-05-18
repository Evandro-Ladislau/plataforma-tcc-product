import logging
import sys

class LoggingConfig:
    @staticmethod
    def setup_logging():
        # Define um formato de log personalizado
        log_format = '{asctime}\t{levelname}\t{message}\n'
        logging.basicConfig(level=logging.DEBUG, format=log_format, style='{')

        # Obtém o logger
        logger = logging.getLogger()

        # Adiciona um handler para redirecionar logs para stdout
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(logging.Formatter(log_format, style='{'))
        logger.addHandler(stdout_handler)


