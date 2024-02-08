#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Pushing files around using shutil and os from the standard library"""

# import additional code to comeplete our task
import shutil
import os

def main():
    """code to move file around"""
    # move into the working directory
    os.chdir("/home/student/mycode/")

    # copy the file! to fileB
     shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_netowrk.txt.copy")

    # copy the entire directoryA to directoryB
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()


