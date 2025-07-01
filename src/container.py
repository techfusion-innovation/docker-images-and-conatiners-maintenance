import logging

import docker

logger = logging.getLogger(__name__)


def clean_old_containers() -> None:
    """
    Clean up old containers that are not running.
    """
    pass
    client = docker.DockerClient(base_url="unix://var/run/docker.sock")
    containers: list = client.containers.list(all=True)
    for container in containers:
        if container.status != "running":
            try:
                container.remove(force=True)
                logger.info(f"Removed container: {container.name}")
            except docker.errors.APIError as e:
                logger.error(f"Failed to remove container {container.name}")
                logger.exception(e)
