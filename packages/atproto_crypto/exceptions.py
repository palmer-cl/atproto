from atproto_core.exceptions import AtProtocolError


class InvalidCompressedPubkeyError(AtProtocolError):
    ...


class DidKeyError(AtProtocolError):
    ...


class IncorrectMultikeyPrefixError(DidKeyError):
    ...


class UnsupportedKeyTypeError(DidKeyError):
    ...
