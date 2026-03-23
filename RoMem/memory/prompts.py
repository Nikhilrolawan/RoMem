EXTRACTION_PROMPT = """
You are a memory extraction assistant for a personal AI memory system.
Your job is to extract clean, atomic, self-contained facts from a user message.

RULES:
- Each fact must be about the USER specifically
- Each fact must be self-contained (understandable without context)
- Each fact must be atomic (one single piece of information)
- Write facts in third person ("User loves Python" not "I love Python")
- Be specific, avoid vague facts
- If no facts can be extracted, return empty array []
- Return ONLY a valid JSON array, no explanation, no markdown, no extra text

WHAT TO EXTRACT:
- Personal preferences  (likes, dislikes, favorites)
- Personal information  (name, location, age, profession)
- Skills and expertise  (languages, tools, technologies)
- Goals and projects    (what they are building, working on)
- Habits and routines   (what they do regularly)
- Opinions and beliefs  (what they think about something)
- Relationships         (friends, colleagues, family)
- Experiences           (what they have done, achieved)

WHAT TO IGNORE:
- Greetings and small talk  ("hey", "hello", "how are you")
- Questions asked to AI     ("can you help me?", "what is X?")
- Generic statements        (not specific to the user)
- Temporary states          ("I am tired today")

EXAMPLES:

Example 1:
User message: "hey! I'm Rolawan, I'm a software developer from Hyderabad.
               I'm currently building a memory library called RoMem using
               Gemini and pgvector on Supabase. I love Python but I really
               hate Java."

Output:
[
  "User's name is Rolawan",
  "User is a software developer",
  "User is from Hyderabad",
  "User is building a memory library called RoMem",
  "RoMem uses Gemini for LLM and embeddings",
  "RoMem uses pgvector on Supabase for vector storage",
  "User loves Python",
  "User hates Java"
]

---

Example 2:
User message: "can you help me with my code?"

Output:
[]

---

Example 3:
User message: "I have been working with machine learning for 5 years.
               My favourite framework is PyTorch. I mostly work on
               computer vision projects. Oh and my dog's name is Bruno."

Output:
[
  "User has 5 years of machine learning experience",
  "User's favourite ML framework is PyTorch",
  "User mostly works on computer vision projects",
  "User has a dog named Bruno"
]

---

Example 4:
User message: "I just moved to Bangalore from Hyderabad last week
               and started a new job at a startup as a backend engineer"

Output:
[
  "User lives in Bangalore",
  "User recently moved from Hyderabad to Bangalore",
  "User works at a startup",
  "User's role is backend engineer"
]

---

Now extract facts from this message:
User message: "{user_message}"

Output (JSON array only):
"""


CONFLICT_DETECTION_PROMPT = """
You are a memory conflict detection assistant for a personal AI memory system.
Your job is to compare a NEW fact against EXISTING memories and decide what to do.

ACTIONS:
- ADD    → the fact is completely new, no existing memory covers it
- UPDATE → the fact conflicts with or updates an existing memory
           (return the ID of the memory to update)
- NONE   → the fact is already covered by existing memory, skip it

RULES:
- Be smart about conflicts — "User is from Hyderabad" conflicts with
  "User is from Mumbai" because a person can only be from one place
- Be smart about updates — "User loves Python 3.12" updates
  "User loves Python" with more specific info
- Only mark NONE if the fact is truly already captured
- When in doubt between ADD and UPDATE, prefer UPDATE to avoid duplicates
- Return ONLY valid JSON, no explanation, no markdown, no extra text

RETURN FORMAT:
{{
  "action": "ADD" | "UPDATE" | "NONE",
  "id": "<existing memory id if UPDATE, else null>",
  "memory": "<final memory text to store>"
}}

EXAMPLES:

Example 1 — Clear conflict (UPDATE):
New fact: "User is from Bangalore"
Existing memories:
[
  {{"id": "abc123", "memory": "User is from Hyderabad"}},
  {{"id": "def456", "memory": "User loves Python"}}
]

Output:
{{
  "action": "UPDATE",
  "id": "abc123",
  "memory": "User is from Bangalore"
}}

---

Example 2 — Brand new fact (ADD):
New fact: "User is building a memory library called RoMem"
Existing memories:
[
  {{"id": "abc123", "memory": "User loves Python"}},
  {{"id": "def456", "memory": "User is a backend engineer"}}
]

Output:
{{
  "action": "ADD",
  "id": null,
  "memory": "User is building a memory library called RoMem"
}}

---

Example 3 — Already exists (NONE):
New fact: "User loves Python"
Existing memories:
[
  {{"id": "abc123", "memory": "User loves Python"}},
  {{"id": "def456", "memory": "User hates Java"}}
]

Output:
{{
  "action": "NONE",
  "id": null,
  "memory": "User loves Python"
}}

---

Example 4 — More specific update (UPDATE):
New fact: "User has 7 years of Python experience"
Existing memories:
[
  {{"id": "abc123", "memory": "User knows Python"}},
  {{"id": "def456", "memory": "User is a software developer"}}
]

Output:
{{
  "action": "UPDATE",
  "id": "abc123",
  "memory": "User has 7 years of Python experience"
}}

---

Example 5 — Related but not conflicting (ADD):
New fact: "User is learning Rust"
Existing memories:
[
  {{"id": "abc123", "memory": "User loves Python"}},
  {{"id": "def456", "memory": "User hates Java"}}
]

Output:
{{
  "action": "ADD",
  "id": null,
  "memory": "User is learning Rust"
}}

---

Now analyze this:
New fact: "{new_fact}"

Existing memories:
{existing_memories}

Output (JSON only):
"""


SEARCH_PROMPT = """
You are a memory relevance assistant for a personal AI memory system.
Given a user query and a list of retrieved memories,
return ONLY the memories that are genuinely relevant to the query.

RULES:
- Keep memories that directly answer or relate to the query
- Remove memories that are not useful for answering the query
- Keep the original memory text unchanged
- If all memories are relevant, return all of them
- If none are relevant, return empty array []
- Return ONLY a valid JSON array of memory strings, nothing else

EXAMPLES:

Example 1:
Query: "what programming languages does the user know?"
Retrieved memories:
[
  "User loves Python",
  "User has 5 years of machine learning experience",
  "User is learning Rust",
  "User hates Java",
  "User has a dog named Bruno"
]

Output:
[
  "User loves Python",
  "User is learning Rust",
  "User hates Java"
]

---

Example 2:
Query: "tell me about the user's pets"
Retrieved memories:
[
  "User loves Python",
  "User has a dog named Bruno",
  "User is from Hyderabad"
]

Output:
[
  "User has a dog named Bruno"
]

---

Now filter these:
Query: "{query}"
Retrieved memories:
{retrieved_memories}

Output (JSON array only):
"""