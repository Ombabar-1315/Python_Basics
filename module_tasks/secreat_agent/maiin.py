import agent

name = input("Enter your name: ")
city = input("Enter your city: ")


print("===========================")
print("🕵️ SECRET AGENT SYSTEM")
print("===========================")
print()

print("Agent Name :",name)
print("Location :",city)

id = agent.generate_agent_id()
code = agent.generate_agent_code()
print()
print(f"Agent Id   :AG-{id}")
print("Agent Code :",code)

print()



print()

if city == "solapur":
    print("MISSION STATUS : Active! ")

else:
    print("MISSION STATUS : Pending")


print("======================================")

agent.genrate_agent(
    "Python",
    "Cybersecurity",
    "Networking",
    name="Om",
    city="Solapur"
)