pragma solidity 0.5.1;

contract Constant {
   
    uint a;

    
    function test_view_shadow() public view{
        uint a;
        a = 0;
    }

    function test_view() public view{
        a;
    }

    function test_assembly_bug() public view{
        assembly{}
    }
}
