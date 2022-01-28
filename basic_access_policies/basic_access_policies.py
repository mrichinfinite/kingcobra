# Imports
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.infra
import cobra.model.pol
import cobra.model.phys
import cobra.model.l3ext
import cobra.model.fvns
import cobra.model.fv
import cobra.model.ospf
import cobra.model.vns
import cobra.model.vz
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
lacpLagPol = cobra.model.lacp.LagPol(infraInfra, annotation='', ctrl='fast-sel-hot-stdby,graceful-conv,susp-individual', descr='', maxLinks='16', minLinks='1', mode='active', name='LACP_Active', nameAlias='', ownerKey='', ownerTag='')

# Switch profile
infraNodeP = cobra.model.infra.NodeP(infraInfra, annotation='', descr='', name='Leaf101_102', nameAlias='', ownerKey='', ownerTag='')
infraRsAccPortP = cobra.model.infra.RsAccPortP(infraNodeP, annotation='', tDn='uni/infra/accportprof-Leaf101_102')
infraLeafS = cobra.model.infra.LeafS(infraNodeP, annotation='', descr='', name='Leaf101_102', nameAlias='', ownerKey='', ownerTag='', type='range')
infraNodeBlk = cobra.model.infra.NodeBlk(infraLeafS, annotation='', descr='', from_='101', name='ff16139dc666a0f2', nameAlias='', to_='102')

# Interface profile
infraAccPortP = cobra.model.infra.AccPortP(infraInfra, annotation='', descr='', name='Leaf101_102', nameAlias='', ownerKey='', ownerTag='')
infraHPortS = cobra.model.infra.HPortS(infraAccPortP, annotation='', descr='', name='Eth1_1-2', nameAlias='', ownerKey='', ownerTag='', type='range')
infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101', tDn='uni/infra/funcprof/accbundle-vPC')
infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1', fromPort='1', name='block2', nameAlias='', toCard='1', toPort='2')

# Interface selector
infraHPortS = cobra.model.infra.HPortS(infraAccPortP, annotation='', descr='', name='Eth1_1-2', nameAlias='', ownerKey='', ownerTag='', type='range')
infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation='', fexId='101', tDn='uni/infra/funcprof/accbundle-vPC')
infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation='', descr='', fromCard='1', fromPort='1', name='block2', nameAlias='', toCard='1', toPort='2')

# Interface policy group
infraAccBndlGrp = cobra.model.infra.AccBndlGrp(infraFuncP, annotation='', descr='', lagT='node', name='vPC', nameAlias='', ownerKey='', ownerTag='')
infraRsStpIfPol = cobra.model.infra.RsStpIfPol(infraAccBndlGrp, annotation='', tnStpIfPolName='')
infraRsQosLlfcIfPol = cobra.model.infra.RsQosLlfcIfPol(infraAccBndlGrp, annotation='', tnQosLlfcIfPolName='')
infraRsQosIngressDppIfPol = cobra.model.infra.RsQosIngressDppIfPol(infraAccBndlGrp, annotation='', tnQosDppPolName='')
infraRsStormctrlIfPol = cobra.model.infra.RsStormctrlIfPol(infraAccBndlGrp, annotation='', tnStormctrlIfPolName='')
infraRsQosEgressDppIfPol = cobra.model.infra.RsQosEgressDppIfPol(infraAccBndlGrp, annotation='', tnQosDppPolName='')
infraRsMonIfInfraPol = cobra.model.infra.RsMonIfInfraPol(infraAccBndlGrp, annotation='', tnMonInfraPolName='')
infraRsMcpIfPol = cobra.model.infra.RsMcpIfPol(infraAccBndlGrp, annotation='', tnMcpIfPolName='')
infraRsMacsecIfPol = cobra.model.infra.RsMacsecIfPol(infraAccBndlGrp, annotation='', tnMacsecIfPolName='')
infraRsQosSdIfPol = cobra.model.infra.RsQosSdIfPol(infraAccBndlGrp, annotation='', tnQosSdIfPolName='')
infraRsAttEntP = cobra.model.infra.RsAttEntP(infraAccBndlGrp, annotation='', tDn='uni/infra/attentp-AEP')
infraRsCdpIfPol = cobra.model.infra.RsCdpIfPol(infraAccBndlGrp, annotation='', tnCdpIfPolName='CDP_Enabled')
infraRsL2IfPol = cobra.model.infra.RsL2IfPol(infraAccBndlGrp, annotation='', tnL2IfPolName='')
infraRsQosDppIfPol = cobra.model.infra.RsQosDppIfPol(infraAccBndlGrp, annotation='', tnQosDppPolName='')
infraRsCoppIfPol = cobra.model.infra.RsCoppIfPol(infraAccBndlGrp, annotation='', tnCoppIfPolName='')
infraRsLldpIfPol = cobra.model.infra.RsLldpIfPol(infraAccBndlGrp, annotation='', tnLldpIfPolName='LLDP_Enabled')
infraRsFcIfPol = cobra.model.infra.RsFcIfPol(infraAccBndlGrp, annotation='', tnFcIfPolName='')
infraRsQosPfcIfPol = cobra.model.infra.RsQosPfcIfPol(infraAccBndlGrp, annotation='', tnQosPfcIfPolName='')
infraRsHIfPol = cobra.model.infra.RsHIfPol(infraAccBndlGrp, annotation='', tnFabricHIfPolName='')
infraRsL2PortSecurityPol = cobra.model.infra.RsL2PortSecurityPol(infraAccBndlGrp, annotation='', tnL2PortSecurityPolName='')
infraRsL2PortAuthPol = cobra.model.infra.RsL2PortAuthPol(infraAccBndlGrp, annotation='', tnL2PortAuthPolName='')
infraRsLacpPol = cobra.model.infra.RsLacpPol(infraAccBndlGrp, annotation='', tnLacpLagPolName='LACP_Active')
infraRsLinkFlapPol = cobra.model.infra.RsLinkFlapPol(infraAccBndlGrp, annotation='', tnFabricLinkFlapPolName='')

# AEP
infraAttEntityP = cobra.model.infra.AttEntityP(infraInfra, annotation='', descr='', name='AEP', nameAlias='', ownerKey='', ownerTag='')
infraRsDomP2 = cobra.model.infra.RsDomP(infraAttEntityP, annotation='', tDn='uni/phys-Phys_Dom')

# Physical domain
physDomP = cobra.model.phys.DomP(polUni, annotation='', name='Phys_Dom', nameAlias='', ownerKey='', ownerTag='')
infraRsVlanNs = cobra.model.infra.RsVlanNs(physDomP, annotation='', tDn='uni/infra/vlanns-[VLAN_Pool]-dynamic')

# VLAN pool
fvnsVlanInstP = cobra.model.fvns.VlanInstP(infraInfra, allocMode='dynamic', annotation='', descr='', name='VLAN_Pool', nameAlias='', ownerKey='', ownerTag='')
fvnsEncapBlk = cobra.model.fvns.EncapBlk(fvnsVlanInstP, allocMode='static', annotation='', descr='', from_='vlan-100', name='', nameAlias='', role='external', to='vlan-199')

# vPC domain
fabricProtPol = cobra.model.fabric.ProtPol(fabricInst, annotation='', descr='', name='default', nameAlias='', ownerKey='', ownerTag='', pairT='explicit')
fabricExplicitGEp = cobra.model.fabric.ExplicitGEp(fabricProtPol, annotation='', id='1', name='101-102-VPG')
fabricRsVpcInstPol = cobra.model.fabric.RsVpcInstPol(fabricExplicitGEp, annotation='', tnVpcInstPolName='')
fabricNodePEp = cobra.model.fabric.NodePEp(fabricExplicitGEp, annotation='', descr='', id='102', name='', nameAlias='', podId='1')
fabricNodePEp2 = cobra.model.fabric.NodePEp(fabricExplicitGEp, annotation='', descr='', id='101', name='', nameAlias='', podId='1')

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
