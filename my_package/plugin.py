from rayforge.core.hooks import hookimpl


@hookimpl
def rayforge_init(context):
    """Called when the application context is fully initialized."""
    print("My Awesome Package has been loaded!")


@hookimpl
def on_unload():
    """Called when the addon is being disabled or unloaded."""
    print("My Awesome Package is being unloaded!")


@hookimpl
def register_producers(producer_registry):
    """Register custom producers. Called in backend context."""
    pass


@hookimpl
def register_steps(step_registry):
    """Register custom steps. Called in backend context."""
    pass
