from algopy import ARC4Contract, String, arc4, subroutine

class HelloWorld(ARC4Contract):
    
    @arc4.abimethod()
    def greet(self, name: String) -> String:
        return "Hello " + name

@subroutine
def create_new_application() -> None:
    hello_world_app = arc4.arc4_create(HelloWorld).created_app

    greeting, _txn = arc4.abi_call(HelloWorld.greet, "there", app_id=hello_world_app)
    
    assert greeting == "Hello there"