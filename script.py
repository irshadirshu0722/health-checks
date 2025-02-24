import sys
def main():
  checks = [
    (check_root_full,"Root partition full")
  ]
  everything_ok  = True
  for check,msg in checks:
    print(msg)
    everything_ok = False
  if not everything_ok:
    sys.exit(1)
  for check,msg in checks:
    print(msg)
    everything_ok = False
  if not everything_ok:
    sys.exit(1)
  print("Everything fine!")
  return


def check_root_full():
  """ Returns True if the root partition is full, False otherwise"""
  
def check_cpu():
  """Return True if cpu is working fine otherwise False"""

print("Main function is going to run")
main()
print("We are here")
print("We are not here")
print("hi everyone")
 
