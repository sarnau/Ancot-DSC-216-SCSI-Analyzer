8-Apr-03

The two .BIN files in this archive represent the last revisions made of system EPROM and the ANTEST Disk Exerciser program for the Ancot DSC-216 SCSI Bus Analyzer. Both files are in Absolute Binary (Data I/O #16) format, and should therefore be readable and usable with any standard device programmer that recognizes binary formats.

The files are as follows.

216V262.BIN: System EPROM. Use a 27C2002-15 or faster UV-EPROM. Install in socket U1 on the motherboard. Checksum-16 for the file should be 93ED. Note that if you load the image into a Data I/O UniSite system, it may read the checksum as a Checksum-8 figure. If that's the case, the last four characters of the result should still be 93ED.

ANTST200.BIN: ANTEST Disk Exerciser Utility. Use a 27C010-15 or faster UV-EPROM. Install in socket U2 on the motherboard. Checksum-16 for this file should be 0D06. If your programming system gives you a Checksum-8 figure instead, the last four characters should still be 0D06.

IMPORTANT NOTE: BEFORE YOU INSTALL THIS UPDATE -- CHECK the version checksums of PAL chips U35 and U48 on the motherboard. They should be labeled or stamped with the codes 'BB22A' and 'BB21A' respectively. IF YOU HAVE DIFFERENT NUMBERS ON YOUR CHIPS, THE UPGRADE WILL NOT BOOT. Your system will hang, just after the power-up test, with the 'Tracing' light on steady, and 'System Reset' will not have any effect.

Good luck!

