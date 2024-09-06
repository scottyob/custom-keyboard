# custom-keyboard
My very first custom keyboard!

## Goals
* Be really quick to change machines from a work computer, personal computer, and embedded computer
* Have an embeded display for e-mails and custom notifications.

## Designing
[Keyboard Layout Editor](http://www.keyboard-layout-editor.com/) is used to build the layout
[PCB Generator](https://builder.mrkeebs.com/) is used to build the base KiCad templates - Not working
[KiCad plugin](https://github.com/adamws/kicad-kbplacer) Maybe this

## Inspiration
https://github.com/overlordpro-sys/keycool84keyboard
[Designers Guide](https://wiki.ai03.com/books/pcb-design/chapter/pcb-designer-guide)
[Great YouTube Design](https://www.youtube.com/watch?v=8WXpGTIbxlQ) (plus, his name is Scotto!)

## Display options
* This looks small enough and has a large enough resolution to be useful:  https://www.amazon.com/Portable-Computer-Temperature-Raspberry-Monitoring/dp/B0C5CJSM3B/ref=sr_1_15?crid=1Z2TTTSMCJ9M3&dib=eyJ2IjoiMSJ9.twG_gHx_7npwcecLIDkTMz68C16EEFkX2myDhWZpakM4PwJHDKMsepyzzZx5_fr-Fv0QWtuMAJvjoFRniusn_2mAP8U1p1KvTDTy_nIf5XBhxKDMTtR6kEIH5bDDDC3kfiqdF0MrOl_FwFwhKsGs7nZMyqzwkf1SLikeBaauqQMlMwHEYTlBRP9wpbAJ9CpN7bQet1QICcqR2IB1Qb4BmEeEdJr8Al8KNutdiwxeoi11xH34oSaYqEw22Ke8fPJI00CEKSvfC8BukvGODd5jw-uKOd0040SWEzb48uFr6ig.ORM6r5WaZxyWdhVOk3N-LtFBRF50ZFboxtpqMb3Jbdg&dib_tag=se&keywords=stretched%2Bbar%2Bdisplay&qid=1719265894&sprefix=stretched%2Bbar%2Bdisplay%2Caps%2C145&sr=8-15&th=1


## Log
The KeyCool 84 model was used

## BOM
Keys:  https://www.amazon.com/Ranked-Ks-33-Switches-Mechanical-Keyboards/dp/B09WYFZ9RW?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=AH4D7YJ4IREB6&th=1

Switches:  Keychron Low-Profile Keychron Optical White Switch Set:  https://www.amazon.com/Keychron-Low-Profile-Optical-White-Switch/dp/B09F8N5671/ref=asc_df_B09F8N5671/?tag=hyprod-20&linkCode=df0&hvadid=692875362841&hvpos=&hvnetw=g&hvrand=16111957698866127215&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9031967&hvtargid=pla-2281435178578&mcid=0d9c4b6c974f36919238ca352fcf1e5d&hvocijid=16111957698866127215-B09F8N5671-&hvexpln=73&gad_source=1&th=1

---
Keys:  https://nuphy.com/products/nuphy-wisteria-t55-low-profile-switches?variant=40519244185709&currency=USD&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&cmp_id=20374253646&adg_id=&kwd=&device=c&gad_source=1&gclid=CjwKCAjw-O6zBhASEiwAOHeGxY04Fqa9ekofnuaXTJEuknBaLYsXi4nRFtKgb14qA1gg2Q-BrQMgmBoCAmcQAvD_BwE

[200~NuPhy Wisteria Low-profile Switches

**You'll want Gateron KS-33**


Use These:  https://shop.beekeeb.com/product/gateron-low-profile-hotswap-socket/
With this footprint:  https://github.com/siderakb/key-switches.pretty?tab=readme-ov-file#user-content-fn-pth-25bb5443dc34dca477740638b10eb813


Guides:
https://github.com/ebastler/zmk-designguide
this recommends holyiot 18010 or moko mk08a. other people fiddle around with stuff like xiao nrf or even nice!nano (or nice!nano clones)

Keycaps perhaps:
- These are not shine through, but I like them!  https://www.amazon.com/Chocfox-Keyboard-Switches-Mechanical-white-134Keys/dp/B0CQ1ZHDP8/ref=sims_dp_d_dex_ai_speed_loc_mtl-v2_v1_d_sccl_2_5/139-4689362-5463854?pd_rd_w=tRYy4&content-id=amzn1.sym.970de5f6-e09a-4fcf-80c0-0a0041912886&pf_rd_p=970de5f6-e09a-4fcf-80c0-0a0041912886&pf_rd_r=KBXG3AW2HWJMRZ1WNTVA&pd_rd_wg=QhR4F&pd_rd_r=f35a1bc3-d88b-4c73-8d4c-3228ac4289e8&pd_rd_i=B0CQ1ZHDP8&psc=1

- Yeah, I think these keycaps:  https://www.amazon.com/XVX-Profile-Keyboard-Switches-Mechanical/dp/B0BVYV67QS/ref=pd_bxgy_thbs_d_sccl_1/139-4689362-5463854?pd_rd_w=X4Tbp&content-id=amzn1.sym.60707ad7-5cf4-45ed-b044-7f953897a39a&pf_rd_p=60707ad7-5cf4-45ed-b044-7f953897a39a&pf_rd_r=VAWAKCYHR6X9TYQKH0A8&pd_rd_wg=gBP03&pd_rd_r=466d4956-36b8-48f1-ac49-e200315451c7&pd_rd_i=B0BVYV67QS&psc=1


 - Controller

Probably this:  https://makerdiary.com/products/nrf52840-connectkit?variant=43255093035163



# Setup
1. Install [This Plugin](https://github.com/ebastler/marbastlib)
2. 

Footprint for KS-33:  https://shop.beekeeb.com/product/gateron-low-profile-hotswap-socket/