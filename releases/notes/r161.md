**r161 — peak pro plasma** · 1.61.0 · 2026-10-02 · phase 5, world depth

### Summary

Peak Pro Plasma. A Peak never bonded with this computer is bonded before Lorax (one PUP or SiLabs version read, as puff.social does), the limits are asked for before the access seed, and a request with no answer names itself. The device list shows Puffco devices only (services, manufacturer id 3075, Peak/Puffco names, address prefixes), with a box to show everything. Verified: audits clean; a simulated unbonded Peak times out on r160 and completes the handshake on r161; smoke clean (r161 in the title). Not tested on a real Plasma.

### Patch notes

**State: r161 / 1.61.0, sealed 2026-10-02 ("Peak Pro Plasma").** The owner,
on r160: "it still will not connect … lorax connection times out every
single time", on a Peak Pro Plasma bought recently, and asked whether the
code only connects to the original Peak Pro; also for Bluetooth filtering
("I don't need to see TVs and stuff"), and about long load times.

**Next:** the owner's test on the Plasma, desktop app and Chrome both. If it
still times out, the error now names the request the Peak did not answer;
that is where to look.

### Why a new Peak timed out

A Peak that has never bonded with the computer accepts the connection, the
version read and the reply subscription, then never answers a Lorax request.
The connect flow (written against the owner's older Peak, bonded with this
computer long before) deliberately did not read anything that would start a
bond — "Do not read PUP … either action can make the device buzz and
re-enter pairing mode repeatedly" — so on the new Plasma the setup request
and then the access-seed request went unanswered, and the seed's 5 s timeout
was the error the owner saw every time. puff.social, whose Lorax client this
one follows, reads the PUP app version (or, without PUP, the SiLabs version)
before anything else, commented "This triggers pairing on lorax", then asks
for the limits (`GET_LIMITS`, 0x02) before the access seed. r161 does the
same: the PUP and SiLabs services are requested, one version read starts the
bond, the limits come first, and a request that gets no answer now says
which request it was. Nothing written to the device changed.

Shown with a simulated Peak in the harness that ignores every request until
its PUP version has been read: on r160 the setup request and the seed went
unanswered (the owner's failure); on r161 the bond read came first and the
limits, setup, seed and unlock requests all followed. That proves the order,
not the device: the simulation is built on what puff.social does, and no
Plasma was available here.

### Only Puffco devices in the list

The device request filters for Puffco now: any device advertising the
Lorax, legacy, PUP or SiLabs service, Puffco's Bluetooth manufacturer id
(3075), a name starting Peak or Puffco, or one still named by its address
with one of the prefixes puff.social lists for Puffco devices (what an
unrenamed Peak advertises). A box under Connect, "show every nearby
Bluetooth device", lists everything, for a Peak renamed past all of those.

### Load time

Timed in the harness with marks at every world stream: the boot script
finishes at 6.3 s on r158 and 7.2 s on r161 (software rendering; the
residents' kit is most of the second). That is not the "crazy" load the
owner saw. The portable `.exe` unpacks its whole app (about 100 MB) into a
temporary folder on every launch, which the installed version does not; the
setup `.exe` is the one to use day to day. Not measured on Windows.

### Verified

- `check-parse`, `audit-source` (B and C 0), `audit-dom`, `audit-dead`
  (668, 0 dead), `audit-comments`, `test-switch-frames`, `test-switch-b9`:
  clean.
- The simulated Peak, r160 against r161, as above; the request options
  carry 105 filters and the four services.
- Smoke: game booted, bridge, chooser installed, `requestDevice` settles,
  "Emberwatch — r161".
- Variants 6/6 built, 6/6 booted.
- Not run: the runtime audit; a real Peak.

### In the code

- 4.97 MB (+3,522 bytes on r160).
- No functions added or removed.

### Play it

Download the `.html` below and open it in a Chromium browser (Chrome or Edge): the whole game is that one file. Chrome can also use Web Bluetooth from a local HTML file on supported systems; browser, OS and adapter support still matter. The newest release also includes the Windows desktop app, with its own Bluetooth chooser and pairing prompts.
