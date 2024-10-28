import algopy
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
        algopy.itxn.AssetTransfer(asset_receiver=receiver, xfer_asset=asset, amount=amount).submit()
    @algopy.arc4.abimethod()
    def opt_into_asset(self,asset:algopy.Asset)-> None:
        self._onlyOwner()
        algopy.itxn.AssetTransfer(asset_receiver=algopy.Txn.sender, xfer_asset=asset)
    

