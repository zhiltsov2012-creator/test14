from aiogram.fsm.state import State, StatesGroup

class TechLeaderQuest(StatesGroup):
    vug = State()
    sit1 = State()
    sit2 = State()
    sit3 = State()
    # roadmap отдельно не храним в FSM, просто callback