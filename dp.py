
import os
from supabase import create_client

url = os.getenv("https://asyxmwjaouffiqkueyvy.supabase.co")
key = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFzeXhtd2phb3VmZmlxa3VleXZ5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODUwNzI0NjAsImV4cCI6MjEwMDY0ODQ2MH0.t4wEUefv7kq0GSGdqtJRnQKJSFibseyBLCgel3FwLR0")

supabase = create_client(url, key)
