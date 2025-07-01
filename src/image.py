import logging

import docker

logger = logging.getLogger(__name__)


def clean_old_images() -> None:
    """Clean up old Docker images that are not associated with any running containers."""
    client = docker.DockerClient(base_url="unix://var/run/docker.sock")
    images = client.images.list(all=True)
    for image in images:
        try:
            # Check if the image is associated with any running container
            if not image.attrs["RepoTags"]:
                client.images.remove(image.id, force=True)
                logger.info(f"Removed image: {image.id}")
        except docker.errors.APIError as e:
            logger.error(f"Error removing image {image.id}")
            logger.exception(e)
