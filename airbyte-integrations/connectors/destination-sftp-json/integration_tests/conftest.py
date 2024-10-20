#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def docker_compose_file() -> Path:
    return Path(__file__).parent.absolute() / "docker-compose.yml"


@pytest.fixture(scope="session")
def sftp_service(docker_ip, docker_services):
    """Ensure that SFTP service is up and responsive."""
    # `port_for` takes a container port and returns the corresponding host port
    port = docker_services.port_for("ssh", 22)
    docker_services.wait_until_responsive(timeout=30.0, pause=0.1, check=lambda: is_ssh_ready(docker_ip, port))
    return docker_ip
