#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
module: vcenter_vm_guest_networking_routes_info
short_description: Collect the guest networking routes information
description: Collect the guest networking routes information
options:
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
    - Virtual machine ID
    - The parameter must be the id of a resource returned by M(vcenter_vm_info). Required
      with I(state=['list'])
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
- name: Get guest network routes information
  vcenter_vm_guest_networking_routes_info:
    vm: '{{ test_vm1_info.id }}'
"""

RETURN = """
# content generated by the update_return_section callback# task: Get guest network routes information
value:
  description: Get guest network routes information
  returned: On success
  sample:
  - gateway_address: 192.168.122.1
    interface_index: 0
    network: 0.0.0.0
    prefix_length: 0
  - interface_index: 0
    network: 192.168.122.0
    prefix_length: 24
  - interface_index: 0
    network: 'fe80::'
    prefix_length: 64
  - interface_index: 0
    network: fe80::9acf:792d:e1af:34ef
    prefix_length: 128
  - interface_index: 0
    network: 'ff00::'
    prefix_length: 8
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {"list": {"query": {}, "body": {}, "path": {"vm": "vm"}}}

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
    }

    argument_spec["vm"] = {"type": "str"}

    return argument_spec


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    session = await open_session(
        vcenter_hostname=module.params["vcenter_hostname"],
        vcenter_username=module.params["vcenter_username"],
        vcenter_password=module.params["vcenter_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def build_url(params):

    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return (
        "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/guest/networking/routes"
    ).format(**params) + gen_args(params, _in_query_parameters)


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url) as resp:
        _json = await resp.json()
        if module.params.get("None"):
            _json["id"] = module.params.get("None")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, url)
        else:  # list context, retrieve the details of each entry
            try:
                if (
                    isinstance(_json["value"][0]["None"], str)
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
