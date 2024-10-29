#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

import json
import pathlib

import asyncclick as click
from connector_ops.utils import console  # type: ignore
from pipelines.cli.dagger_pipeline_command import DaggerPipelineCommand
from rich.table import Table
from rich.text import Text


@click.command(cls=DaggerPipelineCommand, help="List all selected connectors.", name="list")
@click.option("--output-file", type=click.Path(exists=False, writable=True, path_type=pathlib.Path), help="Output file path.", default=None)
@click.pass_context
async def list_connectors(
    ctx: click.Context,
    output_file: pathlib.Path,
) -> bool:
    selected_connectors = sorted(ctx.obj["selected_connectors_with_modified_files"], key=lambda x: x.technical_name)
    table = Table(title=f"{len(selected_connectors)} selected connectors")
    table.add_column("Modified")
    table.add_column("Connector")
    table.add_column("Language")
    table.add_column("Release stage")
    table.add_column("Version")
    table.add_column("Folder")


    connector_dicts = []
    for connector in selected_connectors:
        connector_dicts.append({
            "name": connector.technical_name,
            "language": connector.language.value if connector.language else None,
            "support_level": connector.support_level if connector.support_level else None,
            "version": connector.version if connector.version else None,
            "folder": str(connector.code_directory),
            "modified": bool(connector.modified_files),  
        })
        
        modified = "X" if connector.modified_files else ""
        connector_name = Text(connector.technical_name)
        language: Text = Text(connector.language.value) if connector.language else Text("N/A")
        try:
            support_level: Text = Text(connector.support_level)
        except Exception:
            support_level = Text("N/A")
        try:
            version: Text = Text(connector.version)
        except Exception:
            version = Text("N/A")
        folder = Text(str(connector.code_directory))
        table.add_row(modified, connector_name, language, support_level, version, folder)

    console.print(table)
    output_file.write_text(json.dumps(connector_dicts, indent=2))
    console.print(f"List of selected connectors written to {output_file}")
    return True
