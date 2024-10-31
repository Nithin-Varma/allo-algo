import algopy
from algopy import Contract, ARC4Contract, String, Account, UInt64, UInt256
from algopy.arc4 import DynamicArray, Address, Struct


class PayoutSummary(Struct):
    recipientAddress: Address
    amount: UInt256

class BaseStrategy(ARC4Contract):
    def __init__(self, alloContractId: Account, strategyId:String) -> None:
        self.alloContractId = alloContractId
        self.strategyId = strategyId
        self.poolActive: bool = false
        self.poolId = UInt64(0)
        self.poolAmount = UInt256(0)

    def __OnlyAllo(self) -> None :
        assert(algopy.Txn.sender == self.alloContractId, "only allo contract can call this function")

    def __OnlyInitialized(self) -> None :
        assert(self.poolId !=0, "pool is not initialized")

    def getAlloContractId(self) -> Account :
        return self.alloContractId

    def getPoolId(self) -> UInt64 :
        return self.poolId

    def getStrategyId(self) -> Account :
        return self.strategyId

    def getPoolAmount(self) -> Account :
        return self.poolAmount

    def isPoolActive(self) -> bool :
        return self.poolActive
    
    def baseStrategy_init(self, _poolId: UInt256) -> None :
        self.__OnlyAllo()
        assert(self.poolId == 0, "pool already initialized")
        assert(_poolId != 0, "invalid pool id")
        self.poolId = _poolId
    
    def increasePoolAmount(self, _amount: UInt256) -> None :
        self.__OnlyAllo()
        self.poolAmount += _amoount

    def registerRecipient(self, _data: Bytes, _sender: Account) -> Account :
        self.__OnlyAllo()
        self.__OnlyInitialized()
        _beforeRegisterRecipient(_data, _sender)
        recipientId: Account = _registerRecipient(_data, _sender)
        _afterRegisterRecipient(_data, _sender)

    def allocate(self, _data: Bytes, _sender: Account) :
        self.__OnlyAllo()
        _beforeAllocate(_data, _sender)
        _allocate(_data, _sender)
        _afterAllocate(_data, _sender)

    def distribute(self, _recipientIds: DynamicArray[Address], _data: Bytes, _sender: Account):
        self.__OnlyAllo()
        self.__OnlyInitialized()
        _beforeDistribute(_recipientIds, _data, _sender)
        _distribute(_recipientIds, _data, _sender)
        _afterDistribute(_recipientIds,_data, _sender)

    # def getPayOuts(self, _recipientIds: DynamicArray[Address], _data: DynamicArray[Bytes]) :
    #     assert(_recipientIds.length == _data.length, "recipient and data length mismatch")
        
        

    # receipient register
    @algopy.subroutine   
    def _registerRecipient(self, _data: Bytes, _sender: Account) -> Account:

    @algopy.subroutine
    def _beforeRegisterRecipient(self, data: Bytes, sender: Account):
        pass

    @algopy.subroutine
    def _afterRegisterRecipient(self, data: Bytes, sender: Account):
        pass

    # allocate
    @algopy.subroutine   
    def _allocate(self, _data: Bytes, _sender: Account) -> Account:

    @algopy.subroutine
    def _beforeAllocate(self, data: Bytes, sender: Account):
        pass

    @algopy.subroutine
    def _afterAllocate(self, data: Bytes, sender: Account):
        pass

    # distribute
    @algopy.subroutine   
    def _distribute(self, _recipientIds: DynamicArray[Address], _data: Bytes, _sender: Account):

    @algopy.subroutine
    def _beforeDistribute(self, _recipientIds: DynamicArray[Address], _data: Bytes, sender: Account):
        pass

    @algopy.subroutine
    def _afterDistribute(self, _recipientIds: DynamicArray[Address], _data: Bytes, sender: Account):
        pass

    # @algopy.subroutine
    # def _getPayOut(self, _recipientId: Address, _data: Bytes):
    #     pass