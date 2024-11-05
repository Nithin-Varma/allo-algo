import algopy
import algopy.arc4 as arc4
VERSION = 1

class Anchor(algopy.ARC4Contract):
    def __init__(self) -> None:
        self.owner = algopy.Account()
    @algopy.arc4.abimethod()
    def create(self, owner: algopy.Account) -> None:
        assert (
            self.owner == algopy.Account()
        ), "Contract has already been initialized"
        self.owner = owner
    @algopy.subroutine
    def _onlyOwner(self) -> None:
        assert (
            algopy.Txn.sender == self.owner
        ), "Only the account set in global_state.owner may call this method"
    @algopy.arc4.abimethod()
    def transferAlgo(self,receiver:algopy.Account,amount:algopy.UInt64)-> None:
        self._onlyOwner()
        algopy.itxn.Payment(receiver=receiver, amount=amount).submit()
    @algopy.arc4.abimethod()
    def transferAsset(self,receiver:algopy.Account,asset:algopy.Asset,amount:algopy.UInt64)-> None:
        self._onlyOwner()
        algopy.itxn.AssetTransfer(asset_receiver=receiver, xfer_asset=asset, asset_amount=amount).submit()
    @algopy.arc4.abimethod()
    def opt_into_asset(self,asset:algopy.Asset)-> None:
        self._onlyOwner()
        algopy.itxn.AssetTransfer(asset_receiver=algopy.Txn.sender, xfer_asset=asset,asset_amount=algopy.UInt64(0)).submit()


class Profile(arc4.Struct):
    id: arc4.DynamicBytes
    nonce: arc4.UInt256
    name: arc4.String
    metadata: arc4.String
    owner: arc4.Address
    anchor: arc4.UInt64
    members: arc4.DynamicArray[arc4.Address]

class Registry(algopy.ARC4Contract):
    def __init__(self) -> None:
        self.version = algopy.BigUInt(VERSION)
        self.anchorToProfileId = algopy.BoxMap(algopy.UInt64,algopy.Bytes)
        self.profilesById = algopy.BoxMap(algopy.Bytes,Profile)
        self.profileApplicationIdToPendingAnchor = algopy.BoxMap(algopy.BigUInt,algopy.Account)
    
    @arc4.abimethod()
    def getProfileById(self, id: algopy.Bytes) -> Profile:
        return self.profilesById[id]
    
    @arc4.abimethod()
    def createAnchor(self) -> arc4.Address:
        anchor_app = arc4.arc4_create(Anchor,fee=1000000).created_app
        return arc4.Address.from_bytes(anchor_app.address.bytes)
