from slither import Slither
from slither.core.declarations.function import FunctionType
from slither.core.solidity_types.elementary_type import ElementaryType

"""
tests for `slither.core.declarations.Function`.
tests that `tests/test_function.sol` gets translated into correct
`slither.core.declarations.Function` objects or its subclasses
and that these objects behave correctly.
"""


def test_functions():
    slither = Slither("tests/test_function.sol")
    functions = slither.contracts_as_dict["TestFunction"].available_functions_as_dict()

    f = functions["external_payable(uint256)"]
    assert f.name == "external_payable"
    assert f.full_name == "external_payable(uint256)"
    assert f.canonical_name == "TestFunction.external_payable(uint256)"
    assert f.solidity_signature == "external_payable(uint256)"
    assert f.signature_str == "external_payable(uint256) returns(uint256)"
    assert f.function_type == FunctionType.NORMAL
    assert not f.contains_assembly
    assert not f.can_reenter()
    assert not f.can_send_eth()
    assert not f.is_constructor
    assert not f.is_fallback
    assert not f.is_receive
    assert f.payable
    assert f.visibility == "external"
    assert not f.view
    assert not f.pure
    assert f.is_implemented
    assert not f.is_empty
    assert f.parameters[0].name == "_a"
    assert f.parameters[0].type == ElementaryType("uint256")
    assert f.return_type[0] == ElementaryType("uint256")

    f = functions["public_reenter()"]
    assert f.name == "public_reenter"
    assert f.full_name == "public_reenter()"
    assert f.canonical_name == "TestFunction.public_reenter()"
    assert f.solidity_signature == "public_reenter()"
    assert f.signature_str == "public_reenter() returns()"
    assert f.function_type == FunctionType.NORMAL
    assert not f.contains_assembly
    assert f.can_reenter()
    assert not f.can_send_eth()
    assert not f.is_constructor
    assert not f.is_fallback
    assert not f.is_receive
    assert not f.payable
    assert f.visibility == "public"
    assert not f.view
    assert not f.pure
    assert f.is_implemented
    assert not f.is_empty
    assert not f.parameters
    assert not f.return_type

    f = functions["public_payable_reenter_send(bool)"]
    assert f.name == "public_payable_reenter_send"
    assert f.full_name == "public_payable_reenter_send(bool)"
    assert f.canonical_name == "TestFunction.public_payable_reenter_send(bool)"
    assert f.solidity_signature == "public_payable_reenter_send(bool)"
    assert f.signature_str == "public_payable_reenter_send(bool) returns()"
    assert f.function_type == FunctionType.NORMAL
    assert not f.contains_assembly
    assert f.can_reenter()
    assert f.can_send_eth()
    assert not f.is_constructor
    assert not f.is_fallback
    assert not f.is_receive
    assert f.payable
    assert f.visibility == "public"
    assert not f.view
    assert not f.pure
    assert f.is_implemented
    assert not f.is_empty
    assert f.parameters[0].name == "_b"
    assert f.parameters[0].type == ElementaryType("bool")
    assert not f.return_type

    f = functions["external_send(uint8)"]
    assert f.name == "external_send"
    assert f.full_name == "external_send(uint8)"
    assert f.canonical_name == "TestFunction.external_send(uint8)"
    assert f.solidity_signature == "external_send(uint8)"
    assert f.signature_str == "external_send(uint8) returns()"
    assert f.function_type == FunctionType.NORMAL
    assert not f.contains_assembly
    assert f.can_reenter()
    assert f.can_send_eth()
    assert not f.is_constructor
    assert not f.is_fallback
    assert not f.is_receive
    assert not f.payable
    assert f.visibility == "external"
    assert not f.view
    assert not f.pure
    assert f.is_implemented
    assert not f.is_empty
    assert f.parameters[0].name == "_c"
    assert f.parameters[0].type == ElementaryType("uint8")
    assert not f.return_type

    f = functions["internal_assembly(bytes)"]
    assert f.name == "internal_assembly"
    assert f.full_name == "internal_assembly(bytes)"
    assert f.canonical_name == "TestFunction.internal_assembly(bytes)"
    assert f.solidity_signature == "internal_assembly(bytes)"
    assert f.signature_str == "internal_assembly(bytes) returns(uint256)"
    assert f.function_type == FunctionType.NORMAL
    assert f.contains_assembly
    assert not f.can_reenter()
    assert not f.can_send_eth()
    assert not f.is_constructor
    assert not f.is_fallback
    assert not f.is_receive
    assert not f.payable
    assert f.visibility == "internal"
    assert not f.view
    assert not f.pure
    assert f.is_implemented
    assert not f.is_empty
    assert f.parameters[0].name == "_d"
    assert f.parameters[0].type == ElementaryType("bytes")
    assert f.return_type[0] == ElementaryType("uint256")

    f = functions["fallback()"]
    assert f.name == "fallback"
    assert f.full_name == "fallback()"
    assert f.canonical_name == "TestFunction.fallback()"
    assert f.solidity_signature == "fallback()"
    assert f.signature_str == "fallback() returns()"
    assert f.function_type == FunctionType.FALLBACK
    assert not f.contains_assembly
    assert not f.can_reenter()
    assert not f.can_send_eth()
    assert not f.is_constructor
    assert f.is_fallback
    assert not f.is_receive
    assert not f.payable
    assert f.visibility == "external"
    assert not f.view
    assert not f.pure
    assert f.is_implemented
    assert f.is_empty
    assert not f.parameters
    assert not f.return_type
