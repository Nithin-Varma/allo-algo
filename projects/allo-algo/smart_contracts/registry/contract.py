# from typing import Literal
# from algopy import ARC4Contract, String,BigUInt,BoxMap,Account,Bytes,arc4,Application,itxn, subroutine
# import algopy
# from algopy.arc4 import abimethod,Struct

# VERSION = 1

# # ANCHOR_APPROVAL_CONTRACT_BYTES :bytes = "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuYW5jaG9yLmNvbnRyYWN0LkFuY2hvci5hcHByb3ZhbF9wcm9ncmFtOgogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgIGJueiBtYWluX2VudHJ5cG9pbnRAMgogICAgY2FsbHN1YiBfX2luaXRfXwoKbWFpbl9lbnRyeXBvaW50QDI6CiAgICBjYWxsc3ViIF9fcHV5YV9hcmM0X3JvdXRlcl9fCiAgICByZXR1cm4KCgovLyBzbWFydF9jb250cmFjdHMuYW5jaG9yLmNvbnRyYWN0LkFuY2hvci5fX3B1eWFfYXJjNF9yb3V0ZXJfXygpIC0+IHVpbnQ2NDoKX19wdXlhX2FyYzRfcm91dGVyX186CiAgICAvLyBjb250cmFjdC5weToyCiAgICAvLyBjbGFzcyBBbmNob3IoYWxnb3B5LkFSQzRDb250cmFjdCk6CiAgICBwcm90byAwIDEKICAgIHR4biBOdW1BcHBBcmdzCiAgICBieiBfX3B1eWFfYXJjNF9yb3V0ZXJfX19iYXJlX3JvdXRpbmdAOAogICAgbWV0aG9kICJjcmVhdGUoYWNjb3VudCl2b2lkIgogICAgbWV0aG9kICJ0cmFuc2ZlckFsZ28oYWNjb3VudCx1aW50NjQpdm9pZCIKICAgIG1ldGhvZCAidHJhbnNmZXJBc3NldChhY2NvdW50LGFzc2V0LHVpbnQ2NCl2b2lkIgogICAgbWV0aG9kICJvcHRfaW50b19hc3NldChhc3NldCl2b2lkIgogICAgdHhuYSBBcHBsaWNhdGlvbkFyZ3MgMAogICAgbWF0Y2ggX19wdXlhX2FyYzRfcm91dGVyX19fY3JlYXRlX3JvdXRlQDIgX19wdXlhX2FyYzRfcm91dGVyX19fdHJhbnNmZXJBbGdvX3JvdXRlQDMgX19wdXlhX2FyYzRfcm91dGVyX19fdHJhbnNmZXJBc3NldF9yb3V0ZUA0IF9fcHV5YV9hcmM0X3JvdXRlcl9fX29wdF9pbnRvX2Fzc2V0X3JvdXRlQDUKICAgIGludCAwCiAgICByZXRzdWIKCl9fcHV5YV9hcmM0X3JvdXRlcl9fX2NyZWF0ZV9yb3V0ZUAyOgogICAgLy8gY29udHJhY3QucHk6NQogICAgLy8gQGFsZ29weS5hcmM0LmFiaW1ldGhvZCgpCiAgICB0eG4gT25Db21wbGV0aW9uCiAgICAhCiAgICBhc3NlcnQgLy8gT25Db21wbGV0aW9uIGlzIE5vT3AKICAgIHR4biBBcHBsaWNhdGlvbklECiAgICBhc3NlcnQgLy8gaXMgbm90IGNyZWF0aW5nCiAgICAvLyBjb250cmFjdC5weToyCiAgICAvLyBjbGFzcyBBbmNob3IoYWxnb3B5LkFSQzRDb250cmFjdCk6CiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAxCiAgICBidG9pCiAgICB0eG5hcyBBY2NvdW50cwogICAgLy8gY29udHJhY3QucHk6NQogICAgLy8gQGFsZ29weS5hcmM0LmFiaW1ldGhvZCgpCiAgICBjYWxsc3ViIGNyZWF0ZQogICAgaW50IDEKICAgIHJldHN1YgoKX19wdXlhX2FyYzRfcm91dGVyX19fdHJhbnNmZXJBbGdvX3JvdXRlQDM6CiAgICAvLyBjb250cmFjdC5weToxNgogICAgLy8gQGFsZ29weS5hcmM0LmFiaW1ldGhvZCgpCiAgICB0eG4gT25Db21wbGV0aW9uCiAgICAhCiAgICBhc3NlcnQgLy8gT25Db21wbGV0aW9uIGlzIE5vT3AKICAgIHR4biBBcHBsaWNhdGlvbklECiAgICBhc3NlcnQgLy8gaXMgbm90IGNyZWF0aW5nCiAgICAvLyBjb250cmFjdC5weToyCiAgICAvLyBjbGFzcyBBbmNob3IoYWxnb3B5LkFSQzRDb250cmFjdCk6CiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAxCiAgICBidG9pCiAgICB0eG5hcyBBY2NvdW50cwogICAgdHhuYSBBcHBsaWNhdGlvbkFyZ3MgMgogICAgYnRvaQogICAgLy8gY29udHJhY3QucHk6MTYKICAgIC8vIEBhbGdvcHkuYXJjNC5hYmltZXRob2QoKQogICAgY2FsbHN1YiB0cmFuc2ZlckFsZ28KICAgIGludCAxCiAgICByZXRzdWIKCl9fcHV5YV9hcmM0X3JvdXRlcl9fX3RyYW5zZmVyQXNzZXRfcm91dGVANDoKICAgIC8vIGNvbnRyYWN0LnB5OjIwCiAgICAvLyBAYWxnb3B5LmFyYzQuYWJpbWV0aG9kKCkKICAgIHR4biBPbkNvbXBsZXRpb24KICAgICEKICAgIGFzc2VydCAvLyBPbkNvbXBsZXRpb24gaXMgTm9PcAogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgIGFzc2VydCAvLyBpcyBub3QgY3JlYXRpbmcKICAgIC8vIGNvbnRyYWN0LnB5OjIKICAgIC8vIGNsYXNzIEFuY2hvcihhbGdvcHkuQVJDNENvbnRyYWN0KToKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDEKICAgIGJ0b2kKICAgIHR4bmFzIEFjY291bnRzCiAgICB0eG5hIEFwcGxpY2F0aW9uQXJncyAyCiAgICBidG9pCiAgICB0eG5hcyBBc3NldHMKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDMKICAgIGJ0b2kKICAgIC8vIGNvbnRyYWN0LnB5OjIwCiAgICAvLyBAYWxnb3B5LmFyYzQuYWJpbWV0aG9kKCkKICAgIGNhbGxzdWIgdHJhbnNmZXJBc3NldAogICAgaW50IDEKICAgIHJldHN1YgoKX19wdXlhX2FyYzRfcm91dGVyX19fb3B0X2ludG9fYXNzZXRfcm91dGVANToKICAgIC8vIGNvbnRyYWN0LnB5OjI0CiAgICAvLyBAYWxnb3B5LmFyYzQuYWJpbWV0aG9kKCkKICAgIHR4biBPbkNvbXBsZXRpb24KICAgICEKICAgIGFzc2VydCAvLyBPbkNvbXBsZXRpb24gaXMgTm9PcAogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgIGFzc2VydCAvLyBpcyBub3QgY3JlYXRpbmcKICAgIC8vIGNvbnRyYWN0LnB5OjIKICAgIC8vIGNsYXNzIEFuY2hvcihhbGdvcHkuQVJDNENvbnRyYWN0KToKICAgIHR4bmEgQXBwbGljYXRpb25BcmdzIDEKICAgIGJ0b2kKICAgIHR4bmFzIEFzc2V0cwogICAgLy8gY29udHJhY3QucHk6MjQKICAgIC8vIEBhbGdvcHkuYXJjNC5hYmltZXRob2QoKQogICAgY2FsbHN1YiBvcHRfaW50b19hc3NldAogICAgaW50IDEKICAgIHJldHN1YgoKX19wdXlhX2FyYzRfcm91dGVyX19fYmFyZV9yb3V0aW5nQDg6CiAgICAvLyBjb250cmFjdC5weToyCiAgICAvLyBjbGFzcyBBbmNob3IoYWxnb3B5LkFSQzRDb250cmFjdCk6CiAgICB0eG4gT25Db21wbGV0aW9uCiAgICBibnogX19wdXlhX2FyYzRfcm91dGVyX19fYWZ0ZXJfaWZfZWxzZUAxMgogICAgdHhuIEFwcGxpY2F0aW9uSUQKICAgICEKICAgIGFzc2VydCAvLyBpcyBjcmVhdGluZwogICAgaW50IDEKICAgIHJldHN1YgoKX19wdXlhX2FyYzRfcm91dGVyX19fYWZ0ZXJfaWZfZWxzZUAxMjoKICAgIC8vIGNvbnRyYWN0LnB5OjIKICAgIC8vIGNsYXNzIEFuY2hvcihhbGdvcHkuQVJDNENvbnRyYWN0KToKICAgIGludCAwCiAgICByZXRzdWIKCgovLyBzbWFydF9jb250cmFjdHMuYW5jaG9yLmNvbnRyYWN0LkFuY2hvci5jcmVhdGUob3duZXI6IGJ5dGVzKSAtPiB2b2lkOgpjcmVhdGU6CiAgICAvLyBjb250cmFjdC5weTo1LTYKICAgIC8vIEBhbGdvcHkuYXJjNC5hYmltZXRob2QoKQogICAgLy8gZGVmIGNyZWF0ZShzZWxmLCBvd25lcjogYWxnb3B5LkFjY291bnQpIC0+IE5vbmU6CiAgICBwcm90byAxIDAKICAgIC8vIGNvbnRyYWN0LnB5OjgKICAgIC8vIHNlbGYub3duZXIgPT0gYWxnb3B5LkFjY291bnQoKQogICAgaW50IDAKICAgIGJ5dGUgIm93bmVyIgogICAgYXBwX2dsb2JhbF9nZXRfZXgKICAgIGFzc2VydCAvLyBjaGVjayBzZWxmLm93bmVyIGV4aXN0cwogICAgZ2xvYmFsIFplcm9BZGRyZXNzCiAgICA9PQogICAgLy8gY29udHJhY3QucHk6Ny05CiAgICAvLyBhc3NlcnQgKAogICAgLy8gICAgIHNlbGYub3duZXIgPT0gYWxnb3B5LkFjY291bnQoKQogICAgLy8gKSwgIkNvbnRyYWN0IGhhcyBhbHJlYWR5IGJlZW4gaW5pdGlhbGl6ZWQiCiAgICBhc3NlcnQgLy8gQ29udHJhY3QgaGFzIGFscmVhZHkgYmVlbiBpbml0aWFsaXplZAogICAgLy8gY29udHJhY3QucHk6MTAKICAgIC8vIHNlbGYub3duZXIgPSBvd25lcgogICAgYnl0ZSAib3duZXIiCiAgICBmcmFtZV9kaWcgLTEKICAgIGFwcF9nbG9iYWxfcHV0CiAgICByZXRzdWIKCgovLyBzbWFydF9jb250cmFjdHMuYW5jaG9yLmNvbnRyYWN0LkFuY2hvci50cmFuc2ZlckFsZ28ocmVjZWl2ZXI6IGJ5dGVzLCBhbW91bnQ6IHVpbnQ2NCkgLT4gdm9pZDoKdHJhbnNmZXJBbGdvOgogICAgLy8gY29udHJhY3QucHk6MTYtMTcKICAgIC8vIEBhbGdvcHkuYXJjNC5hYmltZXRob2QoKQogICAgLy8gZGVmIHRyYW5zZmVyQWxnbyhzZWxmLHJlY2VpdmVyOmFsZ29weS5BY2NvdW50LGFtb3VudDphbGdvcHkuVUludDY0KS0+IE5vbmU6CiAgICBwcm90byAyIDAKICAgIC8vIGNvbnRyYWN0LnB5OjE4CiAgICAvLyBzZWxmLl9vbmx5T3duZXIoKQogICAgY2FsbHN1YiBfb25seU93bmVyCiAgICAvLyBjb250cmFjdC5weToxOQogICAgLy8gYWxnb3B5Lml0eG4uUGF5bWVudChyZWNlaXZlcj1yZWNlaXZlciwgYW1vdW50PWFtb3VudCkuc3VibWl0KCkKICAgIGl0eG5fYmVnaW4KICAgIGZyYW1lX2RpZyAtMQogICAgaXR4bl9maWVsZCBBbW91bnQKICAgIGZyYW1lX2RpZyAtMgogICAgaXR4bl9maWVsZCBSZWNlaXZlcgogICAgaW50IHBheQogICAgaXR4bl9maWVsZCBUeXBlRW51bQogICAgaW50IDAKICAgIGl0eG5fZmllbGQgRmVlCiAgICBpdHhuX3N1Ym1pdAogICAgcmV0c3ViCgoKLy8gc21hcnRfY29udHJhY3RzLmFuY2hvci5jb250cmFjdC5BbmNob3IuX29ubHlPd25lcigpIC0+IHZvaWQ6Cl9vbmx5T3duZXI6CiAgICAvLyBjb250cmFjdC5weToxMS0xMgogICAgLy8gQGFsZ29weS5zdWJyb3V0aW5lCiAgICAvLyBkZWYgX29ubHlPd25lcihzZWxmKSAtPiBOb25lOgogICAgcHJvdG8gMCAwCiAgICAvLyBjb250cmFjdC5weToxNAogICAgLy8gYWxnb3B5LlR4bi5zZW5kZXIgPT0gc2VsZi5vd25lcgogICAgdHhuIFNlbmRlcgogICAgaW50IDAKICAgIGJ5dGUgIm93bmVyIgogICAgYXBwX2dsb2JhbF9nZXRfZXgKICAgIGFzc2VydCAvLyBjaGVjayBzZWxmLm93bmVyIGV4aXN0cwogICAgPT0KICAgIC8vIGNvbnRyYWN0LnB5OjEzLTE1CiAgICAvLyBhc3NlcnQgKAogICAgLy8gICAgIGFsZ29weS5UeG4uc2VuZGVyID09IHNlbGYub3duZXIKICAgIC8vICksICJPbmx5IHRoZSBhY2NvdW50IHNldCBpbiBnbG9iYWxfc3RhdGUub3duZXIgbWF5IGNhbGwgdGhpcyBtZXRob2QiCiAgICBhc3NlcnQgLy8gT25seSB0aGUgYWNjb3VudCBzZXQgaW4gZ2xvYmFsX3N0YXRlLm93bmVyIG1heSBjYWxsIHRoaXMgbWV0aG9kCiAgICByZXRzdWIKCgovLyBzbWFydF9jb250cmFjdHMuYW5jaG9yLmNvbnRyYWN0LkFuY2hvci50cmFuc2ZlckFzc2V0KHJlY2VpdmVyOiBieXRlcywgYXNzZXQ6IHVpbnQ2NCwgYW1vdW50OiB1aW50NjQpIC0+IHZvaWQ6CnRyYW5zZmVyQXNzZXQ6CiAgICAvLyBjb250cmFjdC5weToyMC0yMQogICAgLy8gQGFsZ29weS5hcmM0LmFiaW1ldGhvZCgpCiAgICAvLyBkZWYgdHJhbnNmZXJBc3NldChzZWxmLHJlY2VpdmVyOmFsZ29weS5BY2NvdW50LGFzc2V0OmFsZ29weS5Bc3NldCxhbW91bnQ6YWxnb3B5LlVJbnQ2NCktPiBOb25lOgogICAgcHJvdG8gMyAwCiAgICAvLyBjb250cmFjdC5weToyMgogICAgLy8gc2VsZi5fb25seU93bmVyKCkKICAgIGNhbGxzdWIgX29ubHlPd25lcgogICAgLy8gY29udHJhY3QucHk6MjMKICAgIC8vIGFsZ29weS5pdHhuLkFzc2V0VHJhbnNmZXIoYXNzZXRfcmVjZWl2ZXI9cmVjZWl2ZXIsIHhmZXJfYXNzZXQ9YXNzZXQsIGFzc2V0X2Ftb3VudD1hbW91bnQpLnN1Ym1pdCgpCiAgICBpdHhuX2JlZ2luCiAgICBmcmFtZV9kaWcgLTEKICAgIGl0eG5fZmllbGQgQXNzZXRBbW91bnQKICAgIGZyYW1lX2RpZyAtMgogICAgaXR4bl9maWVsZCBYZmVyQXNzZXQKICAgIGZyYW1lX2RpZyAtMwogICAgaXR4bl9maWVsZCBBc3NldFJlY2VpdmVyCiAgICBpbnQgYXhmZXIKICAgIGl0eG5fZmllbGQgVHlwZUVudW0KICAgIGludCAwCiAgICBpdHhuX2ZpZWxkIEZlZQogICAgaXR4bl9zdWJtaXQKICAgIHJldHN1YgoKCi8vIHNtYXJ0X2NvbnRyYWN0cy5hbmNob3IuY29udHJhY3QuQW5jaG9yLm9wdF9pbnRvX2Fzc2V0KGFzc2V0OiB1aW50NjQpIC0+IHZvaWQ6Cm9wdF9pbnRvX2Fzc2V0OgogICAgLy8gY29udHJhY3QucHk6MjQtMjUKICAgIC8vIEBhbGdvcHkuYXJjNC5hYmltZXRob2QoKQogICAgLy8gZGVmIG9wdF9pbnRvX2Fzc2V0KHNlbGYsYXNzZXQ6YWxnb3B5LkFzc2V0KS0+IE5vbmU6CiAgICBwcm90byAxIDAKICAgIC8vIGNvbnRyYWN0LnB5OjI2CiAgICAvLyBzZWxmLl9vbmx5T3duZXIoKQogICAgY2FsbHN1YiBfb25seU93bmVyCiAgICAvLyBjb250cmFjdC5weToyNwogICAgLy8gYWxnb3B5Lml0eG4uQXNzZXRUcmFuc2Zlcihhc3NldF9yZWNlaXZlcj1hbGdvcHkuVHhuLnNlbmRlciwgeGZlcl9hc3NldD1hc3NldCxhc3NldF9hbW91bnQ9YWxnb3B5LlVJbnQ2NCgwKSkuc3VibWl0KCkKICAgIGl0eG5fYmVnaW4KICAgIHR4biBTZW5kZXIKICAgIGludCAwCiAgICBpdHhuX2ZpZWxkIEFzc2V0QW1vdW50CiAgICBmcmFtZV9kaWcgLTEKICAgIGl0eG5fZmllbGQgWGZlckFzc2V0CiAgICBpdHhuX2ZpZWxkIEFzc2V0UmVjZWl2ZXIKICAgIGludCBheGZlcgogICAgaXR4bl9maWVsZCBUeXBlRW51bQogICAgaW50IDAKICAgIGl0eG5fZmllbGQgRmVlCiAgICBpdHhuX3N1Ym1pdAogICAgcmV0c3ViCgoKLy8gc21hcnRfY29udHJhY3RzLmFuY2hvci5jb250cmFjdC5BbmNob3IuX19pbml0X18oKSAtPiB2b2lkOgpfX2luaXRfXzoKICAgIC8vIGNvbnRyYWN0LnB5OjMKICAgIC8vIGRlZiBfX2luaXRfXyhzZWxmKSAtPiBOb25lOgogICAgcHJvdG8gMCAwCiAgICAvLyBjb250cmFjdC5weTo0CiAgICAvLyBzZWxmLm93bmVyID0gYWxnb3B5LkFjY291bnQoKQogICAgYnl0ZSAib3duZXIiCiAgICBnbG9iYWwgWmVyb0FkZHJlc3MKICAgIGFwcF9nbG9iYWxfcHV0CiAgICByZXRzdWIK"
# # ANCHOR_CLEAR_CONTRACT_BYTES: bytes = "I3ByYWdtYSB2ZXJzaW9uIDEwCgpzbWFydF9jb250cmFjdHMuYW5jaG9yLmNvbnRyYWN0LkFuY2hvci5jbGVhcl9zdGF0ZV9wcm9ncmFtOgogICAgaW50IDEKICAgIHJldHVybgo="
# class Anchor(algopy.ARC4Contract):
#     def __init__(self) -> None:
#         self.owner = algopy.Account()
#     @algopy.arc4.abimethod()
#     def create(self, owner: algopy.Account) -> None:
#         assert (
#             self.owner == algopy.Account()
#         ), "Contract has already been initialized"
#         self.owner = owner
#     @algopy.subroutine
#     def _onlyOwner(self) -> None:
#         assert (
#             algopy.Txn.sender == self.owner
#         ), "Only the account set in global_state.owner may call this method"
#     @algopy.arc4.abimethod()
#     def transferAlgo(self,receiver:algopy.Account,amount:algopy.UInt64)-> None:
#         self._onlyOwner()
#         algopy.itxn.Payment(receiver=receiver, amount=amount).submit()
#     @algopy.arc4.abimethod()
#     def transferAsset(self,receiver:algopy.Account,asset:algopy.Asset,amount:algopy.UInt64)-> None:
#         self._onlyOwner()
#         algopy.itxn.AssetTransfer(asset_receiver=receiver, xfer_asset=asset, asset_amount=amount).submit()
#     @algopy.arc4.abimethod()
#     def opt_into_asset(self,asset:algopy.Asset)-> None:
#         self._onlyOwner()
#         algopy.itxn.AssetTransfer(asset_receiver=algopy.Txn.sender, xfer_asset=asset,asset_amount=algopy.UInt64(0)).submit()
# class Profile(arc4.Struct):
#     id: arc4.DynamicBytes
#     nonce: arc4.UInt256
#     name: arc4.String
#     metadata: arc4.String
#     owner: arc4.Address
#     anchor: arc4.UInt64
#     memebers: arc4.DynamicArray[arc4.Address]
# class Registry(ARC4Contract):
#     def __init__(self) -> None:
#         self.version = BigUInt(VERSION)
#         self.anchorToProfileId = BoxMap(algopy.UInt64,Bytes)
#         self.profilesById = BoxMap(Bytes,Profile)
#         self.profileApplicationIdToPendingAnchor = BoxMap(BigUInt,Account)
    
#     @arc4.abimethod()
#     def getProfileById(self, id: Bytes) -> Profile:
#         return self.profilesById[id]
    
#     @arc4.abimethod()
#     def getProfileByAnchor(self, anchor: algopy.UInt64) -> Profile:
#         return self.profilesById[self.anchorToProfileId[anchor]]
#     @arc4.abimethod()
#     def createProfile(self, nonce: arc4.UInt256,name:arc4.String,metadata:arc4.String) -> Bytes:
#         id = algopy.op.sha256(algopy.op.concat(nonce.bytes,algopy.Txn.sender.bytes))
#         anchor_app = arc4.arc4_create(Anchor).created_app

        
#         profile = Profile(id=arc4.DynamicBytes.from_bytes(id),nonce=nonce,name=name,metadata=metadata,owner=arc4.Address.from_bytes(algopy.Txn.sender.bytes),anchor=arc4.UInt64.from_bytes(algopy.op.itob(anchor_app.id)),memebers= arc4.DynamicArray(arc4.Address()))

#         self.profilesById[id] = profile.copy()
        
#         self.anchorToProfileId[anchor_app.id] = profile.id.bytes

#         return id
#     @arc4.abimethod()
#     def addMember(self,profileId:Bytes,member:arc4.Address) -> None:
#         profile : Profile = self.profilesById[profileId].copy()
#         profile.memebers.append(member)
#         self.profilesById[profileId] = profile.copy()
    
#     @arc4.abimethod()
#     def updateProfileName(self,profileId:Bytes,name:arc4.String) -> None:
#         self._onlyProfileOwner(profileId)
#         profile = self.profilesById[profileId].copy()
#         profile.name = name
#         self.profilesById[profileId] = profile.copy()
#     @arc4.abimethod()
#     def updateProfileMetadata(self,profileId:Bytes,metadata:arc4.String) -> None:
#         self._onlyProfileOwner(profileId)
#         profile = self.profilesById[profileId].copy()
#         profile.metadata = metadata
#         self.profilesById[profileId] = profile.copy()
#     @arc4.abimethod()
#     def isOwnerOrMemberOfProfile(self,profileId:Bytes,address:arc4.Address) -> bool:
#         profile : Profile = self.profilesById[profileId].copy()
#         members = profile.memebers.copy()
#         isMember = False
#         for member in members:
#             if member == address:
#                 isMember = True
#                 break
        
#         return profile.owner == address or isMember
#     @subroutine
#     def _onlyProfileOwner(self,profileId:Bytes) -> None:
#         profile = self.profilesById[profileId].copy()
#         assert profile.owner == algopy.Txn.sender, "Only the owner of the profile can call this function"
    