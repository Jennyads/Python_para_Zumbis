#Os lingüistas descobriram que as preposições em Googlon são as palavras que começam com uma letra tipo zumbi
#e que terminan com uma letra tipo outras

def preposicoes (txt):
    lista = []
    for p in txt:
        if p[0] in 'zmb':
            if p[-1] not in 'zmb':
                lista.append(p)
    return len(lista)

#os verbos sempre são palavras de 7 letras que terminam numa letra tipo outras
# se um verbo começa com uma letra tipo outras, o verbo está em primeira pessoa.

def verbos (txt):
    lista = []
    for p in txt:
        if len(p) == 7:
            if p[-1] not in 'zmb':
                lista.append(p)
    return len(lista)

def primeira_pessoa(txt):
    lista = []
    for p in txt:
        if len(p) == 7:
            if p[0] not in 'zmb':
                if p[-1] not in 'zmb':
                    lista.append(p)
    return len(lista)

txtB = '''pwbfdmtc jms gswg wvsscb ffq lbrhbn lcxc hcr thc mghts vkgfc nrvfgs dsrdq
tcmfz scqskgsl twgzh whts dqt twtksl lcrdlc dpzrl hwlqvc xcfstz rfkvbr bzmvqp qxrs
jlmwtcs nmjkkmpg kbcbg shdf qxpm qbm hlcnqnw jwhvvrtr kccw njxtbh hbtn lqmxbx krnn hcv
ptqtwp xgnfggb bjdd nfgkxsw kgzcf bgncx rbsfrrcf vjwsjpw jbtcbqm xhhg kfpqcpx bfxlg
qddzdv rvfqp hphjhns xhk npdd gsxm ffkbj gwdxkhr ddqmr jnzznp jzsgkb lcgsgjvh xvsbdw
klzsxz xpjkjxc gth dtrmkn qzcsksd vsdrhj vtlxg kdtxsj sgs chnz bdllcsdl trggnlpd gwbvj
stnhs vqbhj tdhps sgkk mxnswm ghm sqhfcnlk lpwqpn gcgg mjxh prmqclss zfn gplktxj
vkjnkkv fzzx vdslwsdk fxt pnbqqbk ksfgcvw hxfq xxd rvqzhmm ctvfgxzv nrzdkx nsxmr
bnvkmhcl srvc nczkp zbgsxg nmpx vrqq xfmnsjc zszmrfjv cbwjfldn fgn mzpp crjnct cmh cwh
cvdk cslq tvr gggck pfs thfdcpxt fcffvg bwxr bstbzwsx ghhq ldzzlkg zmfkxvms lfn
zzzfchrk lktdlrlx wzjcvj nbbkqjt lthk wnxsmnx dzftkjr fqfqcjtd dzsvqbnx zhprp cqlphsk
cjvrwg fkhr mxrg tdbxnwrg sdcptlln tjsh vbmd vlgfskcx xtkdp ttjcc qtlmgsh kbndtscg nfw
kctx rcltszw hbjr zld npqqm bpcqrhq szzw vbxj ghhmdq nhfptrsg vpkgwcd rkkxqk jhxpngr
qnkfd wvcsmb bgnvwqln gfbrqn rjjp dvfqjqsf rspxz cvrjxjq gtps fbg rdp pbzqnc nssd
rrpzcwp drfrgjx wvcpw fst frp lmz gbb brzbhlns qsjgzzzp jwvbhl pchqk vhpbdwd mwtlm
wbdxk rsfpxl kqt psr bcdktps mrgnflhr fvxsmsbx rqprpvj clnr hdqzjc bndwhjwp fbbkvdhr
mlgtjw ntk pxv nsnv jnwp vtksnpbb lpwl rslljk hsd rzfmdp xlbnkbw ptfhnlc jjc dpptqzc
jgrt jgxn bgg hslbhksz lhld jfdjq mmttm hwjbnqwv dcxggwhc dcnhhltm fttbf xjnjhgh
tchctgjn fvjkmj wkfxqzkx knbhrwgs xmszj smnrwmlv cdbdwsjf grtkzrwh rwmbvt zssswpc cdvr
klhtb bhkwfwxm bdjzlg nnw hnw fkm dzxpk fmvx kwfj vbf bgp frfbhk kvqwc skddwrtg
brgkfqnf xmwth wrmv rzmjrbfb pkj hckr sfbvz vtfbq fmzf tkhnb srd slkbcmj ppq kxgdbxhh
grwpg hxhjznc ttmgnwb lljfz ftkgv fsjmrvcx dljps mtgnc bkwfwfnj npfvr qlgpv hmqhxfpb
vvwtkrf nfchzb phmhxkck ngrngr lvd dgbwpk txlttnpb ppldgl wsmngb xtxsblgt xxtctgsj
pbvtkm pmcmrmvf phcxvpf wtbfv mvclz dvsl tmzxrrg gbjz dtlsp klmjxg fxh svtlgdl vvlhntpt
zgtkjdm lbjrnmt fbbhqvg dwqnsgj bjjcsvms tlpzlxj bcw rtvmzn kjtqpxhw zkvkdxz dcx zqmsnl
rvqw kgsh gbwdh wslrbz pfnpqh mgj kgmq hpzmp kpr jgz bksx lvsbxzv qgzf qcgpc pvf xlt
znjntxpj stgwsc vxgcfc cbvwhf tbxwpk nbjbkrz rgc wps rjlfpch bxqhw nckdtf bsncq
cnsmqxwn mzmlgpp vnxr qgjs vpkpbsn tgmw lbcxxgsf nnmr wbpdssgm nmddl zcbpcbpt twrkx
sdqxsnw lntr rzv hgjjksxf qpnnjwl hbcv fkwkbd ncv plr lmpfkk dpcj jzjbjgp bdttl
wrrdnmjz mxqxqdxc shztl gdzj rntpnh rjrlrfk rncp qlrhnww rdzhzx qnnxhm gtd lqklxr
gpgpqtrc hfhp hxl bnr fpvxzwmx pfrxglb xmchrvwx wbnxl vjxgbs vddhjkq wndwxs mqndvm
hvbncjw pbmlw hzjwqn nfgxqmb pfvnpwj xbwknvmr xtm cnxck qnmtrvx kmhj hdfrtd gqz srlml
ckx pwlhnpgf rkln tvq vjgrlfs vpvwnjtg wbswcvbh dzcjppjm slt zvxhgq xhcvvc rjd xhqdvhmp
nqlnsk hxmjpmnv sjwwc hbjvpw dpmdnz sxpb qznnxl nwnlmbx vdb hgkkwd znsxfqs kqwjtrcg
vhbnd rpgtkzz fmt nmzhrrqn qbqbvpsm kqwxr gvp xvrvsdf pxwt vkdns dpf jwnwz mxpwc xdvs
drrlpnr xvpztf pxzm jtg fvfgnzx qndpq dmzwnfgm jzknzgk clbpzcpd xhxsqp zbfck btzjd jwbt
gwtll kqj wlsdx sdvnw mqpvxk kjdkt frgwz mpqnqr lpj gvc hcdp zpvrdnc ckvmtbvf bddvc
mptrq xrzwj lzlbc pvgkrhd wlkdtjz pslzhzhc qmrr crkxcs jtxhfvr qzd fwrgdmjt cmg xvhcb
zmllbxs mxg plzxjqlk cwnf mqt hlsssh lvmptxcd zdbsvmll wshnn xzrz xsnhn jhg jtkqhh kcsb
bgsfnz mfxmqjn glzb qtwhllw nfkjfn xgw mvssxl hpb vjhlfgld cgfwq qdvjskx ntnhcl ckm
rqrsw dpff krrkl mcs xnk jpnx llw ljhqlbhs njdm gph nwmm bcclbzz wjfktwv mgthn kltqfx
hqntlps bdr dqtswd vqmkgkb pmznqzh mwgf nndtsx xfrmgqqj mvkfdhh qxp pvpcmx mhnhb slw
clvtxn nfpnlr tsssrk rnvdjpc ptkp hrwx zgblvhlj lqrdrz bhtlqhvv mlpkx jsl vlj kbmfjgs
ktzb wrnn ztbcph lxccgcxh bkrhjtsl cbmhp hwswwqg rnwqq srhnz fkvl kcnr qbxwpg hnss gjdn
rnxhwgd jgngwzc kfvg nwkjt rhjtsvv txk szkpmn nnzbqwgs pjjzqkvx bkw dfcbw rffn qph
kckksgp nzn tpqnm znzppsg tvcgnrb zgdsp tqlqrf vjqqxsp pwj pgft cvl cvr cnhgxsd lkd qlw
vwtbh mfxs gbgw'''

txtB = txtB.split()
quantp = preposicoes(txtB)
print(quantp)

quantv = verbos(txtB)
print(quantv)

quantvpp = primeira_pessoa(txtB)
print(quantvpp)
