import docker

def clean_old_containers() -> None:
    """
    Clean up old containers that are not running.
    """
    pass
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    containers: list = client.containers.list(all=True)
    for container in containers:
        if container.status != 'running':
            try:
                container.remove(force=True)
                print(f"Removed container: {container.name}")
            except docker.errors.APIError as e:
                print(f"Error removing container {container.name}: {e}")