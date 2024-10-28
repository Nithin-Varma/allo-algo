from algopy import ARC4Contract, String,BigUInt,BoxMap,Account,Bytes,arc4,Application
import algopy
from algopy.arc4 import abimethod,Struct
VERSION = 1
class Profile(arc4.Struct):
    id: arc4.DynamicBytes
    nonce: arc4.UInt256
    name: arc4.String
    metadata: arc4.String
    owner: arc4.Address
    anchor: arc4.UInt256
class Registry(ARC4Contract):
    def __init__(self) -> None:
        self.version = BigUInt(VERSION)
        self.anchorToProfileId = BoxMap(Account,BigUInt)
        self.profilesById = BoxMap(BigUInt,Profile)

        self.profileApplicationIdToPendingAnchor = BoxMap(BigUInt,Account)
    
    @arc4.abimethod()
    def getProfileById(self, id: BigUInt) -> Profile:
        return self.profilesById[id]
    
    @arc4.abimethod()
    def getProfileByAnchor(self, anchor: Account) -> Profile:
        return self.profilesById[self.anchorToProfileId[anchor]]
    @arc4.abimethod()
    def createProfile(self, nonce: BigUInt,name:String,metadata:String) -> None:
        
        id = algopy.op.sha256(algopy.op.concat(nonce.bytes,algopy.Txn.sender.bytes))
        profile = Profile(id=id,nonce=nonce,name=name,metadata=metadata,owner=algopy.Txn.sender,anchor=nonce)
        # self.profilesById[Profile.id] = Profile
        # self.anchorToProfileId[Profile.anchor] = Profile.id
        # profile = 
    
    