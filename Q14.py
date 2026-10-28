import pickle
import shelve

# Complex class instance to persist
class GameState:
    def __init__(self, player, level, health):
        self.player = player
        self.level = level
        self.health = health

    def __repr__(self):
        return f"GameState(player='{self.player}', level={self.level}, health={self.health})"

def pickle_demo(state):
    """Serializes and restores an object using a binary stream via pickle."""
    filename = "state.pkl"
    
    # Serialize to disk (Write Binary)
    with open(filename, 'wb') as f:
        pickle.dump(state, f)
    print(f"[*] Saved via Pickle: {state}")

    # Restore from disk (Read Binary)
    with open(filename, 'rb') as f:
        restored_state = pickle.load(f)
    print(f"[*] Restored via Pickle: {restored_state}\n")

def shelve_demo(state1, state2):
    """Persists objects to disk using a dictionary-like database via shelve."""
    db_name = "state_db"
    
    # Write to shelve database
    with shelve.open(db_name) as db:
        db['slot1'] = state1
        db['slot2'] = state2
    print(f"[*] Saved multiple objects via Shelve to '{db_name}'")

    # Read from shelve database
    with shelve.open(db_name) as db:
        print(f"[*] Restored from Shelve [slot1]: {db['slot1']}")
        print(f"[*] Restored from Shelve [slot2]: {db['slot2']}")

if __name__ == "__main__":
    # Live Python object states
    state_a = GameState("Alice", level=5, health=80)
    state_b = GameState("Bob", level=12, health=45)

    print("--- Pickle Serialization ---")
    pickle_demo(state_a)

    print("--- Shelve Serialization ---")
    shelve_demo(state_a, state_b)