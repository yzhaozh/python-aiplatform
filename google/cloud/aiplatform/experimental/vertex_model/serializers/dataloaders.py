# -*- coding: utf-8 -*-

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import functools
import inspect
import logging
import sys
from typing import (
    Any,
    Dict,
    List,
    Sequence,
    Tuple,
    Type,
)

from google.api_core import operation
from google.auth import credentials as auth_credentials
from google.cloud.aiplatform import initializer
from google.cloud.aiplatform import utils
from google.cloud.aiplatform.compat.types import encryption_spec as gca_encryption_spec
from google.cloud import aiplatform
                         
try:
    import torch 
except ImportError:
    raise ImportError("PyTorch is not installed. Please install torch to use VertexModel")


def _serialize_remote_dataloader:
    # writes the referenced data to the run-time bucket
    raise NotImplementedError

def _deserialize_remote_dataloader:
    # read the data from a run-time bucket 
    # and reformat to a DataLoader
    raise NotImplementedError

def _serialize_local_dataloader:
    # finds the local source, and copies 
    # data to the user-designated staging bucket
    raise NotImplementedError

def _deserialize_local_dataloader:
    # read the data from user-designated staging bucket and
    # reformat to a DataLoader
    raise NotImplementedError

def _serialize_dataloader:
    # introspect to determine which method is called
    raise NotImplementedError

def _deserialize_dataloader:
    # introspect to determine which method is called
    raise NotImplementedError