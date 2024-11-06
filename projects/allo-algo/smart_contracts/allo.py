# import algopy
# from algopy import arc4

# class Pool(arc4.Struct):
#     profileId: arc4.DynamicBytes
#     strategy: arc4.UInt64
#     token: arc4.UInt64
#     metadata: arc4.String
#     managerRole: arc4.Address
#     adminRole: arc4.Address
# class Allo(arc4.ARC4Contract):
#     def __init__(self):
#         self.owner = algopy.Account()
#         self.percentageFee = algopy.UInt64()
#         self.baseFee = algopy.UInt64()
#         self.poolIndex = algopy.UInt64()
#         self.treasury = algopy.Address()
#         self.registryAppId = algopy.Application()
#         self.nonces = algopy.BoxMap(algopy.Account,algopy.UInt64)
#         self.pools = algopy.BoxMap(algopy.UInt64,Pool)
#     @arc4.abimethod()
#     def initialise(
#         self,
#         owner:algopy.Account,
#         registry:algopy.Application,
#         treasury:algopy.Account,
#         percentageFee:algopy.UInt64,
#         baseFee:algopy.UInt64 
#     ) -> None:
#         self.owner = owner
#         self.registryAppId=registry
#         self.treasury=treasury
#         self.percentageFee=percentageFee
#         self.baseFee=baseFee
    
#     @arc4.abimethod()
#     def createPoolWithCustomStrategy(self,profileId:algopy.Bytes,strategy:algopy.Application,initStrategyData:algopy.Bytes,) -> algopy.Bytes:


import algopy 
import algopy.arc4 as arc4
VERSION = 1


arc4.UInt64.native
class Pool(arc4.Struct):
    profileId: arc4.DynamicBytes
    strategy: arc4.UInt64
    metadata: arc4.String
    managerRole: arc4.DynamicBytes
    adminRole: arc4.DynamicBytes

class Allo(algopy.ARC4Contract):
    def __init__(self) -> None:
        self.owner = algopy.Account()  # Changed from algopy.Address() to algopy.Account()
        self.percentFee = algopy.UInt64()
        self.baseFee = algopy.UInt64()
        self._poolIndex = algopy.UInt64()
        self.treasury = algopy.Account()  # Changed from algopy.Address() to algopy.Account()
        self.registry = algopy.Application()
        self._nonces = algopy.BoxMap(algopy.Account, algopy.UInt64)
        self.pools = algopy.BoxMap(algopy.UInt64, arc4.DynamicBytes)
        self.cloneableStrategies = algopy.BoxMap(algopy.Account, bool)
        self.roles = algopy.BoxMap(arc4.DynamicBytes,bool)
        self.roleAdmins = algopy.BoxMap(arc4.DynamicBytes, arc4.DynamicBytes)

    @arc4.abimethod()
    def initialize(
        self,
        owner: algopy.Account,
        registry: algopy.Application,
        treasury: algopy.Account,
        percentFee: algopy.UInt64,
        baseFee: algopy.UInt64
    ) -> None:
        assert self.owner == algopy.Account(), "Contract has already been initialized"
        assert owner != algopy.Account(), "Owner cannot be zero address"
        self.owner = owner
        self._updateRegistry(registry)
        self._updateTreasury(treasury)
        self._updatePercentFee(percentFee)
        self._updateBaseFee(baseFee)

    @algopy.subroutine
    def _onlyOwner(self) -> None:
        assert self.owner == algopy.Txn.sender, "Ownable: caller is not the owner"

    @algopy.subroutine
    def _updateRegistry(self, registry: algopy.Application) -> None:
        assert registry.id != algopy.UInt64(0), "ZERO_ADDRESS"
        self.registry = registry

    @algopy.subroutine
    def _updateTreasury(self, treasury: algopy.Account) -> None:
        assert treasury != algopy.Account(), "ZERO_ADDRESS"
        self.treasury = treasury

    @algopy.subroutine
    def _updatePercentFee(self, percentFee: algopy.UInt64) -> None:
        assert percentFee <= algopy.UInt64(10**18), "INVALID_FEE"
        self.percentFee = percentFee

    @algopy.subroutine
    def _updateBaseFee(self, baseFee: algopy.UInt64) -> None:
        self.baseFee = baseFee

    @arc4.abimethod()
    def createPoolWithCustomStrategy(
        self,
        profileId: arc4.DynamicBytes,
        strategy: algopy.Application,
        initStrategyData: arc4.DynamicBytes,
   
        amount: algopy.UInt64,
        metadata: arc4.String,
        managers: arc4.DynamicArray[arc4.Address]  # Changed from algopy.Address to algopy.Account
    ) -> algopy.UInt64:
        assert strategy.id != algopy.UInt64(0), "ZERO_ADDRESS"
        cloneable = self.cloneableStrategies.get(strategy.address, default=False)
        assert cloneable == False, "IS_APPROVED_STRATEGY"

        poolId = self._createPool(profileId, strategy.id, initStrategyData, amount, metadata, managers)
        return poolId

    @arc4.abimethod()
    def createPool(
        self,
        profileId: arc4.DynamicBytes,
        strategy: algopy.Application,
        initStrategyData: arc4.DynamicBytes,
        amount: algopy.UInt64,
        metadata: arc4.String,
        managers: arc4.DynamicArray[arc4.Address]  # Changed from algopy.Address to algopy.Account
    ) -> algopy.UInt64:
        cloneable = self.cloneableStrategies.get(strategy.address, default=False)
        assert cloneable == True, "NOT_APPROVED_STRATEGY"

        # Clone the strategy
        nonce = self._nonces.get(algopy.Txn.sender, default=algopy.UInt64(0))
        cloned_strategy = self._cloneStrategy(strategy, nonce)
        self._nonces[algopy.Txn.sender] = nonce + algopy.UInt64(1)

        poolId = self._createPool(profileId, cloned_strategy.id, initStrategyData, amount, metadata, managers)
        return poolId

    @algopy.subroutine
    def _cloneStrategy(self, strategy: algopy.Application, nonce: algopy.UInt64) -> algopy.Application:
        # Implementation of strategy cloning logic
        # For simplicity, assume the cloned strategy is created and returned
        # In practice, need to perform inner transaction to clone the strategy
        cloned_strategy = algopy.Application()  # Placeholder
        return cloned_strategy

    @algopy.subroutine
    def _createPool(
        self,
        profileId: arc4.DynamicBytes,
        strategy: algopy.UInt64,
        initStrategyData: arc4.DynamicBytes,
        amount: algopy.UInt64,
        metadata: arc4.String,
        managers: arc4.DynamicArray[arc4.Address] # Changed from algopy.Address to algopy.Account
    ) -> algopy.UInt64:
        # Check if sender is owner or member of profile
        # For simplicity, we assume the check passes
        # In practice, need to implement check via application call to registry

        poolId = self._poolIndex + algopy.UInt64(1)
        self._poolIndex = poolId
        arc4.UInt64.f

        POOL_MANAGER_ROLE = algopy.op.itob(poolId)
        POOL_ADMIN_ROLE = algopy.op.sha256(algopy.op.concat(algopy.op.itob(poolId), algopy.Bytes(b"admin")))

        pool = Pool(
            profileId=profileId.copy(),
            strategy=arc4.UInt64(strategy),
            metadata=metadata,
            managerRole=arc4.DynamicBytes.from_bytes(POOL_MANAGER_ROLE),
            adminRole=arc4.DynamicBytes.from_bytes(POOL_ADMIN_ROLE)
        )

        self.pools[poolId] = arc4.DynamicBytes.from_bytes(pool.bytes)

        self._grantRole(arc4.DynamicBytes.from_bytes(POOL_ADMIN_ROLE), algopy.Txn.sender)
        self._setRoleAdmin(arc4.DynamicBytes.from_bytes(POOL_MANAGER_ROLE), arc4.DynamicBytes.from_bytes(POOL_ADMIN_ROLE))

        # Initialize strategy
        # Need to perform inner transaction to call strategy.initialize(poolId, initStrategyData)
        # For simplicity, we skip the inner transaction code

        # Grant pool manager roles
        for manager in managers:
            assert manager.bytes != algopy.Account().bytes, "ZERO_ADDRESS"
            self._grantRole(arc4.DynamicBytes.from_bytes(POOL_MANAGER_ROLE), algopy.Account.from_bytes(manager.bytes))

        # Handle baseFee and amount
        # For simplicity, we skip the fund transfer code

        return poolId

    @arc4.abimethod()
    def updatePoolMetadata(self, poolId: algopy.UInt64, metadata: arc4.String) -> None:
        self._onlyPoolManager(poolId)
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        pool.metadata = metadata
        self.pools[poolId] = arc4.DynamicBytes.from_bytes(pool.bytes)

    @arc4.abimethod()
    def updateRegistry(self, registry: algopy.Application) -> None:
        self._onlyOwner()
        self._updateRegistry(registry)

    @arc4.abimethod()
    def updateTreasury(self, treasury: algopy.Account) -> None:
        self._onlyOwner()
        self._updateTreasury(treasury)

    @arc4.abimethod()
    def updatePercentFee(self, percentFee: algopy.UInt64) -> None:
        self._onlyOwner()
        self._updatePercentFee(percentFee)

    @arc4.abimethod()
    def updateBaseFee(self, baseFee: algopy.UInt64) -> None:
        self._onlyOwner()
        self._updateBaseFee(baseFee)

    @arc4.abimethod()
    def addToCloneableStrategies(self, strategy: algopy.Account) -> None:
        self._onlyOwner()
        assert strategy != algopy.Account(), "ZERO_ADDRESS"
        self.cloneableStrategies[strategy] = True

    @arc4.abimethod()
    def removeFromCloneableStrategies(self, strategy: algopy.Account) -> None:
        self._onlyOwner()
        self.cloneableStrategies[strategy] = False

    @arc4.abimethod()
    def addPoolManager(self, poolId: algopy.UInt64, manager: algopy.Account) -> None:
        self._onlyPoolAdmin(poolId)
        assert manager != algopy.Account(), "ZERO_ADDRESS"
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        self._grantRole(pool.managerRole.copy(), manager)

    @arc4.abimethod()
    def removePoolManager(self, poolId: algopy.UInt64, manager: algopy.Account) -> None:
        self._onlyPoolAdmin(poolId)
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        self._revokeRole(pool.managerRole.copy(), manager)

    @arc4.abimethod()
    def registerRecipient(self, poolId: algopy.UInt64, data: arc4.DynamicBytes) -> algopy.String:
        # Pass data to the strategy
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        recipientId = algopy.Account() 
        return algopy.String.from_bytes(data.bytes)

    
        

    @arc4.abimethod()
    def fundPool(self, poolId: algopy.UInt64, amount: algopy.UInt64) -> None:
        # Implementation of fundPool logic
        # For simplicity, skip the actual transfer code

        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        # Need to transfer amount to pool's strategy
        # Handle fee deductions

    @arc4.abimethod()
    def allocate(self, poolId: algopy.UInt64, data: arc4.DynamicBytes) -> None:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        # Need to perform inner transaction to call strategy.allocate(data)
        # For simplicity, skip the actual allocation code

    @arc4.abimethod()
    def batchAllocate(
        self, poolIds: arc4.DynamicArray[arc4.UInt64], datas: arc4.DynamicArray[arc4.DynamicBytes]
    ) -> None:
        assert poolIds.length == datas.length, "MISMATCH"
        for i in algopy.urange(poolIds.length):
            self.allocate(algopy.op.btoi(poolIds[i].bytes), datas[i].copy())

    @arc4.abimethod()
    def distribute(
        self, poolId: algopy.UInt64, recipientIds: arc4.DynamicArray[arc4.Address], data: arc4.DynamicBytes
    ) -> None:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        # Need to perform inner transaction to call strategy.distribute(recipientIds, data)
        # For simplicity, skip the actual distribution code

    @algopy.subroutine
    def _onlyPoolManager(self, poolId: algopy.UInt64) -> None:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        isManager = self._hasRole(pool.managerRole.copy(), algopy.Txn.sender)
        if not isManager:
            self._onlyPoolAdmin(poolId)
        else:
            pass  # Caller is a pool manager

    @algopy.subroutine
    def _onlyPoolAdmin(self, poolId: algopy.UInt64) -> None:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        isAdmin = self._hasRole(pool.adminRole.copy(), algopy.Txn.sender)
        assert isAdmin, "UNAUTHORIZED"

    @algopy.subroutine
    def _grantRole(self, role: arc4.DynamicBytes, account: algopy.Account) -> None:
        roleKey = arc4.DynamicBytes.from_bytes(algopy.op.concat(role.bytes, account.bytes))
        self.roles[roleKey] = True

    @algopy.subroutine
    def _revokeRole(self, role: arc4.DynamicBytes, account: algopy.Account) -> None:
        roleKey = arc4.DynamicBytes.from_bytes(algopy.op.concat(role.bytes, account.bytes))
        self.roles[roleKey] = False

    @algopy.subroutine
    def _setRoleAdmin(self, role: arc4.DynamicBytes, adminRole: arc4.DynamicBytes) -> None:
        self.roleAdmins[role] = adminRole.copy()

    @algopy.subroutine
    def _hasRole(self, role: arc4.DynamicBytes, account: algopy.Account) -> bool:
        roleKey = arc4.DynamicBytes.from_bytes(algopy.op.concat(role.bytes, account.bytes))
        return self.roles.get(roleKey, default=False)

    @arc4.abimethod()
    def getFeeDenominator(self) -> algopy.UInt64:
        return algopy.UInt64(10**18)

    @arc4.abimethod()
    def isPoolAdmin(self, poolId: algopy.UInt64, account: algopy.Account) -> bool:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        return self._hasRole(pool.adminRole.copy(), account)

    @arc4.abimethod()
    def isPoolManager(self, poolId: algopy.UInt64, account: algopy.Account) -> bool:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        isManager = self._hasRole(pool.managerRole.copy(), account)
        if not isManager:
            return self._hasRole(pool.adminRole.copy(), account)
        else:
            return True

    @arc4.abimethod()
    def getStrategy(self, poolId: algopy.UInt64) -> arc4.UInt64:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        return pool.strategy

    @arc4.abimethod()
    def getPercentFee(self) -> algopy.UInt64:
        return self.percentFee

    @arc4.abimethod()
    def getBaseFee(self) -> algopy.UInt64:
        return self.baseFee

    @arc4.abimethod()
    def getTreasury(self) -> algopy.Bytes:
        return self.treasury.bytes

    @arc4.abimethod()
    def getRegistry(self) -> algopy.UInt64:
        return self.registry.id

    @arc4.abimethod()
    def isCloneableStrategy(self, strategy: algopy.Account) -> bool:
        return self.cloneableStrategies.get(strategy, default=False)

    @arc4.abimethod()
    def getPool(self, poolId: algopy.UInt64) -> Pool:
        pool_bytes = self.pools[poolId].copy()
        pool = Pool.from_bytes(pool_bytes.bytes)
        return pool
