# Copyright 2015 ETH Zurich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
:mod:`ext_hdr` --- Extension header utilities
=============================================
"""
# Stdlib
import logging
import struct

# SCION
from lib.defines import L4_PROTOS
from lib.errors import SCIONParseError
from lib.packet.ext_hdr import ExtensionHeader, HopByHopType
from lib.packet.ext.traceroute import TracerouteExt
from lib.types import ExtensionClass

# Dictionary of supported extensions
EXTENSION_MAP = {
    (ExtensionClass.HOP_BY_HOP, HopByHopType.TRACEROUTE): TracerouteExt,
}


def parse_extensions(data, next_hdr):
    """
    Parses the raw data and populates the extension header fields
    accordingly.
    """
    cur_hdr_type = next_hdr
    ext_hdrs = []
    while cur_hdr_type not in L4_PROTOS:
        next_hdr_type, hdr_len, ext_no = struct.unpack(
            "!BBB", data.pop(ExtensionHeader.SUBHDR_LEN))
        # Calculate correct hdr_len in bytes
        hdr_len = (hdr_len + 1) * ExtensionHeader.LINE_LEN
        logging.info("Found extension hdr of type (%d, %d) with len %dB",
                     cur_hdr_type, ext_no, hdr_len)
        try:
            ext_class = EXTENSION_MAP[(cur_hdr_type, ext_no)]
        except KeyError:
            SCIONParseError("Extension (%d, %d) unknown." %
                            (cur_hdr_type, ext_no))
        ext_hdrs.append(
            ext_class(data.pop(hdr_len - ExtensionHeader.SUBHDR_LEN)))
        cur_hdr_type = next_hdr_type
    return ext_hdrs, cur_hdr_type