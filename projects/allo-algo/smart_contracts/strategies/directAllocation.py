import algopy
from algopy import arc4, ARC4Contract, Bytes, subroutine
from algopy.arc4 import DynamicArray, Address, Struct, String, UInt64
from .baseStrategy import (
    BaseStrategy,
    PayoutSummary,
    HelloWorld,
)

class DirectAllocated(arc4.Struct):
    profileId: arc4.UInt64
    profileOwner: arc4.Address
    amount: arc4.UInt64
    token: arc4.Address
    sender: arc4.Address

class Initialized(Struct):
    alloContractId: arc4.Address
    strategyId: arc4.String
    poolId: arc4.UInt64

class DirectAllocation(ARC4Contract):

    def __init__(self) -> None:
        self.alloContractId = Address()
        self.strategyId = String()
        self.poolId = UInt64(0)
        self.base_strategy = arc4.arc4_create(BaseStrategy).created_app

    @arc4.abimethod()
    def initialized(self, _alloContractId: Address, _strategyId: String, _poolId: UInt64) -> None:
        self.alloContractId = _alloContractId
        self.strategyId = _strategyId
        self.poolId = _poolId
        arc4.abi_call(BaseStrategy.initializeVariables, self.alloContractId, self.strategyId, app_id=self.base_strategy)
        arc4.abi_call(BaseStrategy.baseStrategy_init, self.poolId, app_id=self.base_strategy)
        arc4.emit(Initialized(_alloContractId, _strategyId, _poolId))

    @arc4.abimethod()
    def directAllocation(self) -> None :
        
