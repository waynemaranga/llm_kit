from os import (getenv as os_getenv, environ as os_envrion)
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import logging
# import loguru

logger = logging.getLogger(__name__) # 

def get_dotenv_path() -> Path:
    # try cwd...
    dotenv_path = find_dotenv(usecwd=True) # <class 'str'>

    if dotenv_path:
        return Path(dotenv_path)

    return Path(__file__).parent / ".env"

def safely_get_env_var(env_var_name: str):

    # try read from env file...
    try:
        load_dotenv(
            dotenv_path=get_dotenv_path(),
            override=True
            )
        
        env_var = os_getenv(env_var_name)

        if env_var is None:
            logger.info(msg=f"{env_var_name} not found in .env file.")

            # look in environment...
            env_var = os_getenv(env_var_name)

            if env_var is None:
                logger.error(msg=f"{env_var_name} not found in environment variables")
                env_var = ""

        return env_var

    except FileNotFoundError:
        logger.info(msg=f".env file not found. Checking environment variables...")
        env_var = os_getenv(env_var_name)

        if env_var is None:
            logger.error(msg=f"{env_var_name} not found in environment variables")
            return ""

        return env_var

if __name__ == "__main__":
    print(get_dotenv_path())
    print(get_dotenv_path().exists())
    print(get_dotenv_path().is_file())
    print("🐋")