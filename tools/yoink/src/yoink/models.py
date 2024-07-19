# Copyright (c) 2024 Airbyte, Inc., all rights reserved.

from dataclasses import dataclass


@dataclass
class ManifestRecord:
    host: str
    manifest: dict

    @property
    def name(self) -> str:
        return self.host.split(".")[-2]

    @property
    def dir_name(self) -> str:
        return f"source-{self.name}"

    @property
    def manifest_filename(self) -> str:
        return f"{self.host}.yaml"
