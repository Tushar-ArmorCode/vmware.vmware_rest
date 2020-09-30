#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
module: vcenter_vm_hardware_disk_info
short_description: Collect the disk information from a VM
description: Collect the disk information from a VM
options:
  disk:
    description:
    - Virtual disk identifier.
    - The parameter must be the id of a resource returned by M(vcenter_vm_hardware_disk).
      Required with I(state=['get'])
    type: str
  label:
    description: []
    type: str
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
  vm:
    description:
    - Virtual machine identifier.
    - The parameter must be the id of a resource returned by M(vcenter_vm_info).
    type: str
author:
- Goneri Le Bouder (@goneri) <goneri@lebouder.net>
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = """
- name: Collect information about a specific VM
  vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info
- name: Retrieve disk information using the label
  vcenter_vm_hardware_disk_info:
    vm: '{{ test_vm1_info.id }}'
    label: Hard disk 1
- name: Retrieve the disk information from the VM
  vcenter_vm_hardware_disk_info:
    vm: '{{ test_vm1_info.id }}'
"""

RETURN = """
# content generated by the update_return_section callback# task: Retrieve disk information using the label
id:
  description: moid of the resource
  returned: On success
  sample: '2000'
  type: str
value:
  description: Retrieve disk information using the label
  returned: On success
  sample:
    backing:
      type: VMDK_FILE
      vmdk_file: '[rw_datastore] test_vm1_3/test_vm1.vmdk'
    capacity: 17179869184
    label: Hard disk 1
    scsi:
      bus: 0
      unit: 0
    type: SCSI
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "list": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "create": {
        "query": {},
        "body": {
            "backing": "spec/backing",
            "ide": "spec/ide",
            "new_vmdk": "spec/new_vmdk",
            "sata": "spec/sata",
            "scsi": "spec/scsi",
            "type": "spec/type",
        },
        "path": {"vm": "vm"},
    },
    "delete": {"query": {}, "body": {}, "path": {"disk": "disk", "vm": "vm"}},
    "get": {"query": {}, "body": {}, "path": {"disk": "disk", "vm": "vm"}},
    "update": {
        "query": {},
        "body": {"backing": "spec/backing"},
        "path": {"disk": "disk", "vm": "vm"},
    },
}

import socket
import json
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
    }

    argument_spec["disk"] = {"type": "str"}
    argument_spec["label"] = {"type": "str"}
    argument_spec["vm"] = {"type": "str"}

    return argument_spec


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    session = await open_session(
        vcenter_hostname=module.params["vcenter_hostname"],
        vcenter_username=module.params["vcenter_username"],
        vcenter_password=module.params["vcenter_password"],
        log_file=module.params["vcenter_rest_log_file"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def build_url(params):

    if params["disk"]:
        _in_query_parameters = PAYLOAD_FORMAT["get"]["query"].keys()
        return (
            "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/hardware/disk/{disk}"
        ).format(**params) + gen_args(params, _in_query_parameters)
    else:
        _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
        return (
            "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/hardware/disk"
        ).format(**params) + gen_args(params, _in_query_parameters)


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url) as resp:
        _json = await resp.json()
        if module.params.get("disk"):
            _json["id"] = module.params.get("disk")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, url)
        else:  # list context, retrieve the details of each entry
            try:
                if (
                    isinstance(_json["value"][0]["disk"], str)
                    and len(list(_json["value"][0].values())) == 1
                ):
                    # this is a list of id, we fetch the details
                    full_device_list = await build_full_device_list(session, url, _json)
                    _json = {"value": [i["value"] for i in full_device_list]}
            except (TypeError, KeyError, IndexError):
                pass

        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
