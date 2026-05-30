import uuid
import datetime

class DigitalEntity:
    """Represents a digital entity with an identity assigned early."""
    def __init__(self, name, entity_type="Generic", status="PLANNED"):
        # The core concept: Assign a unique identifier BEFORE the entity is fully "born" or operational.
        self.id = str(uuid.uuid4()) # Unique ID generated at the earliest stage
        self.name = name
        self.entity_type = entity_type
        self.status = status # Initial status, e.g., PLANNED, RESERVED
        self.creation_timestamp = datetime.datetime.now()
        self.attributes = {} # Placeholder for future attributes

    def update_status(self, new_status):
        """Updates the status of the entity."""
        print(f"  Updating status for '{self.name}' (ID: {self.id[:8]}...) from '{self.status}' to '{new_status}'")
        self.status = new_status

    def add_attribute(self, key, value):
        """Adds or updates an attribute for the entity."""
        self.attributes[key] = value

    def __str__(self):
        attrs_str = ", ".join([f"{k}: {v}" for k, v in self.attributes.items()])
        return (f"Entity ID: {self.id}\n"
                f"  Name: {self.name}\n"
                f"  Type: {self.entity_type}\n"
                f"  Status: {self.status}\n"
                f"  Created: {self.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"  Attributes: {{{attrs_str}}}")

class EntityRegistry:
    """Manages the lifecycle of digital entities from early planning."""
    def __init__(self):
        self.entities = {} # Stores entities by their unique ID

    def pre_register_entity(self, name, entity_type="IoT Device"):
        """
        Pre-registers an entity, assigning it an ID before it's physically available or fully defined.
        This demonstrates the 'naming before birth' concept.
        """
        entity = DigitalEntity(name, entity_type, status="PLANNED")
        self.entities[entity.id] = entity
        print(f"\n[STEP 1] Pre-registered new '{entity_type}' named '{name}' with ID: {entity.id[:8]}... (Status: {entity.status})")
        return entity.id

    def get_entity(self, entity_id):
        """Retrieves an entity by its unique ID."""
        return self.entities.get(entity_id)

    def process_entity_lifecycle(self, entity_id):
        """Simulates the lifecycle of an entity using its pre-assigned ID."""
        entity = self.get_entity(entity_id)
        if not entity:
            print(f"Error: Entity with ID {entity_id[:8]}... not found.")
            return

        print(f"\n[STEP 2] Starting lifecycle for '{entity.name}' (ID: {entity_id[:8]}...)")

        # Stage 1: Manufacturing/Provisioning
        entity.update_status("MANUFACTURED")
        entity.add_attribute("manufacturer", "Acme Corp")
        entity.add_attribute("serial_number", f"SN-{entity_id[:6].upper()}")
        print(f"  Entity '{entity.name}' now has serial number: {entity.attributes['serial_number']}")

        # Stage 2: Configuration/Deployment
        entity.update_status("CONFIGURED")
        entity.add_attribute("firmware_version", "1.0.0")
        entity.add_attribute("location", "Warehouse A")
        print(f"  Entity '{entity.name}' configured with firmware {entity.attributes['firmware_version']}")

        # Stage 3: Activation/Operational
        entity.update_status("ACTIVE")
        entity.add_attribute("ip_address", "192.168.1.101")
        print(f"  Entity '{entity.name}' is now active and operational.")

        print(f"\n[STEP 3] Final state of '{entity.name}':")
        print(entity)


# --- Main execution ---
if __name__ == "__main__":
    print("--- Demonstrating Early Identity Definition in Digital Systems ---")

    registry = EntityRegistry()

    # Scenario 1: An IoT device is planned
    print("\n--- Scenario 1: Planning for a new batch of IoT devices ---")
    device1_id = registry.pre_register_entity("Smart Sensor Alpha", "IoT Device")
    device2_id = registry.pre_register_entity("Gateway Beta", "Network Gateway")

    # We can now refer to these entities by their IDs even before they exist physically
    # For example, allocating network resources or planning software deployments.
    print("\n[INFO] We have reserved IDs for future devices. We can now plan resources for them.")
    print(f"  Reserved ID for Smart Sensor Alpha: {device1_id[:8]}...")
    print(f"  Reserved ID for Gateway Beta: {device2_id[:8]}...")

    # Scenario 2: The devices go through their lifecycle
    print("\n--- Scenario 2: Devices move through manufacturing and deployment ---")
    registry.process_entity_lifecycle(device1_id)
    registry.process_entity_lifecycle(device2_id)

    # Scenario 3: Retrieving an entity by its early-assigned ID
    print("\n--- Scenario 3: Retrieving an entity by its ID ---")
    retrieved_device = registry.get_entity(device1_id)
    if retrieved_device:
        print(f"\nSuccessfully retrieved entity '{retrieved_device.name}' using its early-assigned ID:")
        print(retrieved_device)
    else:
        print(f"Failed to retrieve entity with ID {device1_id[:8]}...")

    print("\n--- Demonstration Complete ---")
