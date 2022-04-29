# Imports
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.infra
import cobra.model.pol
import cobra.model.phys
import cobra.model.fvns
import cobra.model.cdp
import cobra.model.lldp
import cobra.model.lacp
import cobra.model.fabric
from cobra.internal.codec.xmlcodec import toXMLStr

# Log into APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://<apic-ip-address-or-hostname>', 'username', 'password')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# Top level object on which operations will be made
polUni = cobra.model.pol.Uni('')
infraInfra = cobra.model.infra.Infra(polUni)
infraFuncP = cobra.model.infra.FuncP(infraInfra)
fabricInst = cobra.model.fabric.Inst(polUni)

# Interface policies
cdpIfPol = cobra.model.cdp.IfPol(infraInfra, adminSt='enabled', annotation='', descr='', name='CDP_Enabled', nameAlias='', ownerKey='', ownerTag='')    
lldpIfPol = cobra.model.lldp.IfPol(infraInfra, adminRxSt='enabled', adminTxSt='enabled', annotation='', descr='', name='LLDP_Enabled', nameAlias='', ownerKey='', ownerTag='')

# Switch profile
infraNodeP = cobra.model.infra.NodeP(infraInfra, annotation='', descr='', name='Leaf101', nameAlias='', ownerKey='', ownerTag='')
infraRsAccPortP = cobra.model.infra.RsAccPortP(infraNodeP, annotation='', tDn='uni/infra/accportprof-Leaf101')
infraLeafS = cobra.model.infra.LeafS(infraNodeP, annotation='', descr='', name='Leaf101', nameAlias='', ownerKey='', ownerTag='', type='range')
infraNodeBlk = cobra.model.infra.NodeBlk(infraLeafS, annotation='', descr='', from_='101', name='ff16139dc666a0f2', nameAlias='', to_='101')

# Interface profile
infraAccPortP = cobra.model.infra.AccPortP(infraInfra, annotation='', descr='', name='Leaf101', nameAlias='', ownerKey='', ownerTag='')
# Interface selector
infraHPortS = cobra.model.infra.HPortS(infraAccPortP, annotation='', descr='', name='Eth1_1', nameAlias='', ownerKey='', ownerTag='', type='range')
infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101', tDn='uni/infra/funcprof/accportgrp-Access')
infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1', fromPort='1', name='block2', nameAlias='', toCard='1', toPort='1')

# Interface policy group
infraAccPortGrp = cobra.model.infra.AccPortGrp(infraFuncP, annotation='', descr='', lagT='node', name='Access', nameAlias='', ownerKey='', ownerTag='')
infraRsStpIfPol = cobra.model.infra.RsStpIfPol(infraAccPortGrp, annotation='', tnStpIfPolName='')
# infraRsQosLlfcIfPols = cobra.model.infra.RsQosLlfcIfPol(infraAccPortGrp, annotation='', tnQosLlfcIfPolName='')
infraRsQosIngressDppIfPol = cobra.model.infra.RsQosIngressDppIfPol(infraAccPortGrp, annotation='', tnQosDppPolName='')
infraRsStormctrlIfPol = cobra.model.infra.RsStormctrlIfPol(infraAccPortGrp, annotation='', tnStormctrlIfPolName='')
infraRsQosEgressDppIfPol = cobra.model.infra.RsQosEgressDppIfPol(infraAccPortGrp, annotation='', tnQosDppPolName='')
infraRsMonIfInfraPol = cobra.model.infra.RsMonIfInfraPol(infraAccPortGrp, annotation='', tnMonInfraPolName='')
infraRsMcpIfPol = cobra.model.infra.RsMcpIfPol(infraAccPortGrp, annotation='', tnMcpIfPolName='')
infraRsMacsecIfPol = cobra.model.infra.RsMacsecIfPol(infraAccPortGrp, annotation='', tnMacsecIfPolName='')
infraRsQosSdIfPol = cobra.model.infra.RsQosSdIfPol(infraAccPortGrp, annotation='', tnQosSdIfPolName='')
infraRsAttEntP = cobra.model.infra.RsAttEntP(infraAccPortGrp, annotation='', tDn='uni/infra/attentp-AEP')
infraRsCdpIfPol = cobra.model.infra.RsCdpIfPol(infraAccPortGrp, annotation='', tnCdpIfPolName='CDP_Enabled')
infraRsL2IfPol = cobra.model.infra.RsL2IfPol(infraAccPortGrp, annotation='', tnL2IfPolName='')
infraRsQosDppIfPol = cobra.model.infra.RsQosDppIfPol(infraAccPortGrp, annotation='', tnQosDppPolName='')
infraRsCoppIfPol = cobra.model.infra.RsCoppIfPol(infraAccPortGrp, annotation='', tnCoppIfPolName='')
infraRsLldpIfPol = cobra.model.infra.RsLldpIfPol(infraAccPortGrp, annotation='', tnLldpIfPolName='LLDP_Enabled')
infraRsFcIfPol = cobra.model.infra.RsFcIfPol(infraAccPortGrp, annotation='', tnFcIfPolName='')
infraRsQosPfcIfPol = cobra.model.infra.RsQosPfcIfPol(infraAccPortGrp, annotation='', tnQosPfcIfPolName='')
infraRsHIfPol = cobra.model.infra.RsHIfPol(infraAccPortGrp, annotation='', tnFabricHIfPolName='')
infraRsL2PortSecurityPol = cobra.model.infra.RsL2PortSecurityPol(infraAccPortGrp, annotation='', tnL2PortSecurityPolName='')
infraRsL2PortAuthPol = cobra.model.infra.RsL2PortAuthPol(infraAccPortGrp, annotation='', tnL2PortAuthPolName='')
# infraRsLinkFlapPol = cobra.model.infra.RsLinkFlapPol(infraAccPortGrp, annotation='', tnFabricLinkFlapPolName='')

# AEP
infraAttEntityP = cobra.model.infra.AttEntityP(infraInfra, annotation='', descr='', name='AEP', nameAlias='', ownerKey='', ownerTag='')
infraRsDomP2 = cobra.model.infra.RsDomP(infraAttEntityP, annotation='', tDn='uni/phys-Phys_Dom')

# Physical domain
physDomP = cobra.model.phys.DomP(polUni, annotation='', name='Phys_Dom', nameAlias='', ownerKey='', ownerTag='')
infraRsVlanNs = cobra.model.infra.RsVlanNs(physDomP, annotation='', tDn='uni/infra/vlanns-[VLAN_Pool]-dynamic')

# VLAN pool
fvnsVlanInstP = cobra.model.fvns.VlanInstP(infraInfra, allocMode='dynamic', annotation='', descr='', name='VLAN_Pool', nameAlias='', ownerKey='', ownerTag='')
fvnsEncapBlk = cobra.model.fvns.EncapBlk(fvnsVlanInstP, allocMode='static', annotation='', descr='', from_='vlan-1', name='', nameAlias='', role='external', to='vlan-4094')

# Commit the generated code to APIC
print(toXMLStr(infraInfra))
c = cobra.mit.request.ConfigRequest()
c.addMo(infraInfra)
md.commit(c)

print(toXMLStr(infraAccPortP))
c = cobra.mit.request.ConfigRequest()
c.addMo(infraAccPortP)
md.commit(c)

print(toXMLStr(polUni))
c = cobra.mit.request.ConfigRequest()
c.addMo(polUni)
md.commit(c)

print(toXMLStr(fabricInst))
c = cobra.mit.request.ConfigRequest()
c.addMo(fabricInst)
md.commit(c)

print(toXMLStr(infraFuncP))
c = cobra.mit.request.ConfigRequest()
c.addMo(infraFuncP)
md.commit(c)
