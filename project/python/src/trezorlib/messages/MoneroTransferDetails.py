# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class MoneroTransferDetails(p.MessageType):

    def __init__(
        self,
        out_key: bytes = None,
        tx_pub_key: bytes = None,
        additional_tx_pub_keys: List[bytes] = None,
        internal_output_index: int = None,
        sub_addr_major: int = None,
        sub_addr_minor: int = None,
    ) -> None:
        self.out_key = out_key
        self.tx_pub_key = tx_pub_key
        self.additional_tx_pub_keys = additional_tx_pub_keys if additional_tx_pub_keys is not None else []
        self.internal_output_index = internal_output_index
        self.sub_addr_major = sub_addr_major
        self.sub_addr_minor = sub_addr_minor

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('out_key', p.BytesType, 0),
            2: ('tx_pub_key', p.BytesType, 0),
            3: ('additional_tx_pub_keys', p.BytesType, p.FLAG_REPEATED),
            4: ('internal_output_index', p.UVarintType, 0),
            5: ('sub_addr_major', p.UVarintType, 0),
            6: ('sub_addr_minor', p.UVarintType, 0),
        }