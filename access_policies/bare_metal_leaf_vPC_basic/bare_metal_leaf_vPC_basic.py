# Basic access policies for connecting a bare metal (physical) server/host to ACI via vPC. Change the variables as needed for your environment. Tested and verified on ACI software version 5.2(4e).

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

# Provide login information and establish a connection with the APIC.
ls = cobra.mit.session.LoginSession('https://<apic-ip-address-or-hostname>', '<username>', '<password>')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# ***Top level objects on which operations will be made***

# Policy Universe (polUni): Represents policy definition/resolution universe.
polUni = cobra.model.pol.Uni('')
# Access Instance (infraInfra): A container for all tenant infra configurations.
infraInfra = cobra.model.infra.Infra(polUni)
# Function Profile (infraFuncP): Hypervisor management function that provides the policies used for hypervisor management and connectivity. For example, an endpoint group and encap VLAN.
infraFuncP = cobra.model.infra.FuncP(infraInfra)
# Fabric Instance (fabricInst): A container object for fabric policies.
fabricInst = cobra.model.fabric.Inst(polUni)

# ***INTERFACE POLICIES***

# CDP Interface Policy (cdpIfPol)
'''
The Cisco Discovery Protocol interface policy, which is primarily used to obtain protocol addresses of neighboring devices and discover the platform of those devices. 
CDP can also be used to display information about the interfaces your router uses. 
CDP is media- and protocol-independent, and runs on all Cisco-manufactured equipment including routers, bridges, access servers, and switches.
'''
# Name: The interface policy name.
cdpIfPol_name = 'CDP_Enabled'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
cdpIfPol_annotation = ''
# Description: Specifies a description of the policy definition.
cdpIfPol_descr = 'Interface policy to enable CDP.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
cdpIfPol_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
cdpIfPol_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
cdpIfPol_nameAlias = ''
# Admin state: enabled or disabled? Choose one.
cdpIfPol_adminSt = 'enabled'
# Configure policy:
cdpIfPol = cobra.model.cdp.IfPol(infraInfra, adminSt=cdpIfPol_adminSt, annotation=cdpIfPol_annotation, descr=cdpIfPol_descr, name=cdpIfPol_name, nameAlias=cdpIfPol_nameAlias, ownerKey=cdpIfPol_ownerKey, ownerTag=cdpIfPol_ownerTag)   

# LLDP Interface Policy (lldpIfPol)
'''
The Link Layer Discovery Protocol interface policy, which defines a common configuration that will apply to one or more LLDP interfaces. 
LLDP uses the logical link control (LLC) services to transmit and receive information to and from other LLDP agents.
'''
# Name: The interface policy name.
lldpIfPol_name = 'LLDP_Enabled'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
lldpIfPol_annotation = ''
# Description: Specifies a description of the policy definition.
lldpIfPol_descr = 'Interface policy to enable LLDP.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
lldpIfPol_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
lldpIfPol_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
lldpIfPol_nameAlias = ''
# Receive admin state: enabled or disabled? Choose one.
lldpIfPol_adminRxSt = 'enabled'
# Transmit admin state: enabled or disabled? Choose one.
lldpIfPol_adminTxSt = 'enabled'
# Configure policy:
lldpIfPol = cobra.model.lldp.IfPol(infraInfra, adminRxSt=lldpIfPol_adminRxSt, adminTxSt=lldpIfPol_adminTxSt, annotation=lldpIfPol_annotation, descr=lldpIfPol_descr, name=lldpIfPol_name, nameAlias=lldpIfPol_nameAlias, ownerKey=lldpIfPol_ownerKey, ownerTag=lldpIfPol_ownerTag)

# LACP Policy (lacpLagPol)
'''
The Port Channel policy enables you to bundle several physical ports together to form a single port channel. 
Link Aggregation Control Protocol enables a node to negotiate an automatic bundling of links by sending LACP packets to the peer node.
'''
# Name: The interface policy name.
lacpLagPol_name = 'LACP_Active'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
lacpLagPol_annotation = ''
# Description: Specifies a description of the policy definition.
lacpLagPol_descr = 'Interface policy for LACP active mode.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
lacpLagPol_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
lacpLagPol_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
lacpLagPol_nameAlias = ''
# Mode: Static Channel Mode - On (on), LACP Active (active), LACP Passive (passive), MAC Pinning (mac-pin), MAC Pinning-Physical-NIC-load (mac-pin-nicload) or Use Explicit Failover (explicit-failover)? Choose one.
lacpLagPol_mode = 'active'
# Control: Fast Select Hot Standby Ports (fast-sel-hot-stdby), Graceful Convergence (graceful-conv), Load Defer Member Ports (load-defer), Suspend Individual Port (susp-individual), Symmetric hashing (symmetric-hash)? Choose as many as desired, separate by commas.
lacpLagPol_ctrl = 'fast-sel-hot-stdby,graceful-conv,susp-individual'
# Minimum number of links? Choose a number 1-16.
lacpLagPol_minLinks = '1'
# Maximum number of links? Choose a number 1-16.
lacpLagPol_maxLinks = '16'
# Configure policy:
lacpLagPol = cobra.model.lacp.LagPol(infraInfra, annotation=lacpLagPol_annotation, ctrl=lacpLagPol_ctrl, descr=lacpLagPol_descr, maxLinks=lacpLagPol_maxLinks, minLinks=lacpLagPol_minLinks, mode=lacpLagPol_mode, name=lacpLagPol_name, nameAlias=lacpLagPol_nameAlias, ownerKey=lacpLagPol_ownerKey, ownerTag=lacpLagPol_ownerTag)

# ***SWITCH PROFILE***

# Leaf Profile (infraNodeP)
'''
The node profile enables you to specify which nodes (Example: a leaf) to configure.
'''
# Name: The node policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraNodeP_name = 'Leaf101_102'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraNodeP_annotation = ''
# Description: Specifies a description of the policy definition.
infraNodeP_descr = 'Leaf node profile for leaf nodes 101 and 102.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
infraNodeP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
infraNodeP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraNodeP_nameAlias = ''
# Configure policy:
infraNodeP = cobra.model.infra.NodeP(infraInfra, annotation=infraNodeP_annotation, descr=infraNodeP_descr, name=infraNodeP_name, nameAlias=infraNodeP_nameAlias, ownerKey=infraNodeP_ownerKey, ownerTag=infraNodeP_ownerTag)

# Associated Interface Selector Profile (infraRsAccPortP)
'''
A source relation to the interface profile.
'''
# tDn: The target name of the interface selector policy profile.
infraRsAccPortP_tDn = 'uni/infra/accportprof-Leaf101_102'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsAccPortP_annotation = ''
# Configure policy:
infraRsAccPortP = cobra.model.infra.RsAccPortP(infraNodeP, annotation=infraRsAccPortP_annotation, tDn=infraRsAccPortP_tDn)

# Leaf Selector (infraLeafS)
'''
The leaf selector enables you to select the interface to configure.
'''
# Name: Leaf selector name.
infraLeafS_name = 'Leaf101_102'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraLeafS_annotation = ''
# Description: Specifies a description of the policy definition.
infraLeafS_descr = 'Leaf selector for leaf nodes 101 and 102.'
# Type: Leaf selector type. The type will always be 'range'.
infraLeafS_type = 'range'
# Owner Key: The key for enabling clients to own their data for entity correlation.
infraLeafS_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
infraLeafS_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraLeafS_nameAlias = ''
# Configure policy:
infraLeafS = cobra.model.infra.LeafS(infraNodeP, annotation=infraLeafS_annotation, descr=infraLeafS_descr, name=infraLeafS_name, nameAlias=infraLeafS_nameAlias, ownerKey=infraLeafS_ownerKey, ownerTag=infraLeafS_ownerTag, type=infraLeafS_type)

# Node Block (infraNodeBlk)
'''
A node block is a range of nodes. Each node block begins with the first port and ends with the last port.
'''
# Name: The node block name.
infraNodeBlk_name = 'ff16139dc666a0f2'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraNodeBlk_annotation = ''
# Description: The description of this configuration item.
infraNodeBlk_descr = 'Leaf block 101-102.'
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraNodeBlk_nameAlias = ''
# Starting node in block:
infraNodeBlk_from = '101'
# Ending node in block:
infraNodeBlk_to = '102'
# Configure policy:
infraNodeBlk = cobra.model.infra.NodeBlk(infraLeafS, annotation=infraNodeBlk_annotation, descr=infraNodeBlk_descr, from_=infraNodeBlk_from, name=infraNodeBlk_name, nameAlias=infraNodeBlk_nameAlias, to_=infraNodeBlk_to)

# ***INTERFACE PROFILE***

# Leaf Interface Profile (infraAccPortP)
'''
The interface profile enables you to specify the interface you want to configure.
'''
# Name: The interface profile name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraAccPortP_name = 'Leaf101_102'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraAccPortP_annotation = ''
# Description: Specifies a description of the policy definition.
infraAccPortP_descr = 'Leaf interface profile for leaf nodes 101 and 102.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
infraAccPortP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
infraAccPortP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraAccPortP_nameAlias = ''
# Configure policy:
infraAccPortP = cobra.model.infra.AccPortP(infraInfra, annotation=infraAccPortP_annotation, descr=infraAccPortP_descr, name=infraAccPortP_name, nameAlias=infraAccPortP_nameAlias, ownerKey=infraAccPortP_ownerKey, ownerTag=infraAccPortP_ownerTag)

# Interface Selector (infraHPortS)
'''
The Host Port Selector is used for grouping ports between the node and the host (such as hypervisor).
'''
# Name: The host port selector name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraHPortS_name = 'Eth1_1-2'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraHPortS_annotation = ''
# Description: Specifies a description of the policy definition.
infraHPortS_descr = 'Ethernet interfaces 1/1 and 1/2.'
# Type: The host port selector type. The type will always be 'range'.
infraHPortS_type = 'range'
# Owner Key: The key for enabling clients to own their data for entity correlation.
infraHPortS_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
infraHPortS_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraHPortS_nameAlias = ''
# Configure policy:
infraHPortS = cobra.model.infra.HPortS(infraAccPortP, annotation=infraHPortS_annotation, descr=infraHPortS_descr, name=infraHPortS_name, nameAlias=infraHPortS_nameAlias, ownerKey=infraHPortS_ownerKey, ownerTag=infraHPortS_ownerTag, type=infraHPortS_type)

# Access Access Group (infraRsAccBaseGrp)
'''
A source relation to the access policy group providing port configuration.
'''
# tDn: The target name of the interface policy group to associate to the Access Port selector.
infraRsAccBaseGrp_tDn = 'uni/infra/funcprof/accbundle-vPC'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsAccBaseGrp_annotation = ''
# FEX ID: The interface policy group FEX ID. The default value is '101'.
infraRsAccBaseGrp_fexId = '101'
# Configure policy:
infraRsAccBaseGrp = cobra.model.infra.RsAccBaseGrp(infraHPortS, annotation=infraRsAccBaseGrp_annotation, fexId=infraRsAccBaseGrp_fexId, tDn=infraRsAccBaseGrp_tDn)

# Access Port Block (infraPortBlk)
'''
The port block enables you to specify a range of interfaces.
'''
# Name: The port block name.
infraPortBlk_name = 'block2'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraPortBlk_annotation = ''
# Description: The description of this configuration item.
infraPortBlk_descr = 'Interface block Ethernet 1/1-1/2.'
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraPortBlk_nameAlias = ''
# Starting card in block:
infraPortBlk_fromCard = '1'
# Starting port in block:
infraPortBlk_fromPort = '1'
# Ending card in block:
infraPortBlk_toCard = '1'
# Ending port in block:
infraPortBlk_toPort = '2'
# Configure policy:
infraPortBlk = cobra.model.infra.PortBlk(infraHPortS, annotation=infraPortBlk_annotation, descr=infraPortBlk_descr, fromCard=infraPortBlk_fromCard, fromPort=infraPortBlk_fromPort, name=infraPortBlk_name, nameAlias=infraPortBlk_nameAlias, toCard=infraPortBlk_toCard, toPort=infraPortBlk_toPort)

# ***INTERFACE POLICY GROUP***

# PC/VPC Interface Policy Group (infraAccBndlGrp)
'''
The bundle interface group enables you to specify the interface policy you want to use.
'''
# Name: The bundled ports group name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraAccBndlGrp_name = 'vPC'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraAccBndlGrp_annotation = ''
# Description: Specifies a description of the policy definition.
infraAccBndlGrp_descr = 'Virtual port channel interface policy group.'
# lagT: The bundled ports group link aggregation type: port channel vs virtual port channel. Use 'link' for PC and 'node' for vPC.
infraAccBndlGrp_lagT = 'node'
# Owner Key: The key for enabling clients to own their data for entity correlation.
infraAccBndlGrp_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
infraAccBndlGrp_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraAccBndlGrp_nameAlias = ''
# Configure policy:
infraAccBndlGrp = cobra.model.infra.AccBndlGrp(infraFuncP, annotation=infraAccBndlGrp_annotation, descr=infraAccBndlGrp_descr, lagT=infraAccBndlGrp_lagT, name=infraAccBndlGrp_name, nameAlias=infraAccBndlGrp_nameAlias, ownerKey=infraAccBndlGrp_ownerKey, ownerTag=infraAccBndlGrp_ownerTag)

# Relation to Access STP Interface Policy (infraRsStpIfPol)
'''
A source relation to the spanning-tree protocol (STP) policy.
'''
# Name: The STP Interface Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved. STP policy ensures that loops are not created if there are redundant paths in the network.
infraRsStpIfPol_tnStpIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsStpIfPol_annotation = ''
# Configure policy:
infraRsStpIfPol = cobra.model.infra.RsStpIfPol(infraAccBndlGrp, annotation=infraRsStpIfPol_annotation, tnStpIfPolName=infraRsStpIfPol_tnStpIfPolName)

# Interface Link Level Flow Control (infraRsQosLlfcIfPol) (Relation to Link Level Flow Control Policy)
'''
A source relation to the link level flow control interface policy.
'''
# Name: The Link Level Flow Control Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
# infraRsQosLlfcIfPol_tnQosLlfcIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
# infraRsQosLlfcIfPol_annotation = ''
# Configure policy:
# infraRsQosLlfcIfPol = cobra.model.infra.RsQosLlfcIfPol(infraAccBndlGrp, annotation=infraRsQosLlfcIfPol_annotation, tnQosLlfcIfPolName=infraRsQosLlfcIfPol_tnQosLlfcIfPolName)

# Ingress Data Plane Policing Policy (infraRsQosIngressDppIfPol) (Relation to Data Plane Policing Interface Policy)
'''
A source relation to the data plane policing interface policy as ingress.
'''
# Name: The Ingress Data Plane Policing Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsQosIngressDppIfPol_tnQosDppPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsQosIngressDppIfPol_annotation = ''
# Configure policy:
infraRsQosIngressDppIfPol = cobra.model.infra.RsQosIngressDppIfPol(infraAccBndlGrp, annotation=infraRsQosIngressDppIfPol_annotation, tnQosDppPolName=infraRsQosIngressDppIfPol_tnQosDppPolName)

# Storm Control Interface Policy (infraRsStormctrlIfPol) (Relation to Storm Control Policy)
'''
A source relation to the storm control interface policy.
'''
# Name: The Storm Control Interface Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsStormctrlIfPol_tnStormctrlIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsStormctrlIfPol_annotation = ''
# Configure policy:
infraRsStormctrlIfPol = cobra.model.infra.RsStormctrlIfPol(infraAccBndlGrp, annotation=infraRsStormctrlIfPol_annotation, tnStormctrlIfPolName=infraRsStormctrlIfPol_tnStormctrlIfPolName)

# Egress Data Plane Policing Policy (infraRsQosEgressDppIfPol) (Relation to Data Plane Policing Interface Policy)
'''
A source relation to the data plane policing interface policy as egress.
'''
# Name: The Egress Data Plane Policing Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsQosEgressDppIfPol_tnQosDppPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsQosEgressDppIfPol_annotation = ''
# Configure policy:
infraRsQosEgressDppIfPol = cobra.model.infra.RsQosEgressDppIfPol(infraAccBndlGrp, annotation=infraRsQosEgressDppIfPol_annotation, tnQosDppPolName=infraRsQosEgressDppIfPol_tnQosDppPolName)

# Relation to Access Monitoring Interface Policy (infraRsMonIfInfraPol)
'''
A source relation to the monitoring policy model.
'''
# Name: The Monitoring Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsMonIfInfraPol_tnMonInfraPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsMonIfInfraPol_annotation = ''
# Configure policy:
infraRsMonIfInfraPol = cobra.model.infra.RsMonIfInfraPol(infraAccBndlGrp, annotation=infraRsMonIfInfraPol_annotation, tnMonInfraPolName=infraRsMonIfInfraPol_tnMonInfraPolName)

# Mis-cabling Protocol Interface Policy (infraRsMcpIfPol) (Relation to MCP Policy)
'''
A source relation to the mis-cabling protocol interface policy.
'''
# Name: The MCP Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsMcpIfPol_tnMcpIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsMcpIfPol_annotation = ''
# Configure policy:
infraRsMcpIfPol = cobra.model.infra.RsMcpIfPol(infraAccBndlGrp, annotation=infraRsMcpIfPol_annotation, tnMcpIfPolName=infraRsMcpIfPol_tnMcpIfPolName)

# Relation to MACsec Interface Policy (infraRsMacsecIfPol)
'''
A source relation to the Media Access Control security interface policy.
'''
# Name: The MACsec Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsMacsecIfPol_tnMacsecIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsMacsecIfPol_annotation = ''
# Configure policy:
infraRsMacsecIfPol = cobra.model.infra.RsMacsecIfPol(infraAccBndlGrp, annotation=infraRsMacsecIfPol_annotation, tnMacsecIfPolName=infraRsMacsecIfPol_tnMacsecIfPolName)

# Slow Drain Policy (infraRsQosSdIfPol) (Relation to Slow Drain Interface Policy)
'''
A source relation to the slow drain interface policy.
'''
# Name: The Slow Drain Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsQosSdIfPol_tnQosSdIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsQosSdIfPol_annotation = ''
# Configure policy:
infraRsQosSdIfPol = cobra.model.infra.RsQosSdIfPol(infraAccBndlGrp, annotation=infraRsQosSdIfPol_annotation, tnQosSdIfPolName=infraRsQosSdIfPol_tnQosSdIfPolName)

# Relation to Access Attach Entity Policy (infraRsAttEntP)
'''
A source relation to the attached entity profile.
'''
# tDn: The target name of the Attached Entity Profile. A host or cluster of hosts attached to a profile.
infraRsAttEntP_tDn = 'uni/infra/attentp-AEP'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsAttEntP_annotation = ''
# Configure policy:
infraRsAttEntP = cobra.model.infra.RsAttEntP(infraAccBndlGrp, annotation=infraRsAttEntP_annotation, tDn=infraRsAttEntP_tDn)

# Relation to CDP Interface Policy (infraRsCdpIfPol)
'''
A source relation to the Cisco Discovery Protocol interface policy.
'''
# Name: The CDP Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsCdpIfPol_tnCdpIfPolName = 'CDP_Enabled'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsCdpIfPol_annotation = ''
# Configure policy:
infraRsCdpIfPol = cobra.model.infra.RsCdpIfPol(infraAccBndlGrp, annotation=infraRsCdpIfPol_annotation, tnCdpIfPolName=infraRsCdpIfPol_tnCdpIfPolName)

# Relation to L2 Interface Policy (infraRsL2IfPol)
'''
A source relation to the Layer 2 interface policy.
'''
# Name: The L2 Interface Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsL2IfPol_tnL2IfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsL2IfPol_annotation = ''
# Configure policy:
infraRsL2IfPol = cobra.model.infra.RsL2IfPol(infraAccBndlGrp, annotation=infraRsL2IfPol_annotation, tnL2IfPolName=infraRsL2IfPol_tnL2IfPolName)

# Data Plane Policy Both (infraRsQosDppIfPol) (Relation to Data Plane Policing Interface Policy)
'''
A source relation to the data plane policing interface policy.
'''
# Name: The Data Plane Policing Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsQosDppIfPol_tnQosDppPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsQosDppIfPol_annotation = ''
# Configure policy:
infraRsQosDppIfPol = cobra.model.infra.RsQosDppIfPol(infraAccBndlGrp, annotation=infraRsQosDppIfPol_annotation, tnQosDppPolName=infraRsQosDppIfPol_tnQosDppPolName)

# Relation to per interface per protocol CoPP Policy (infraRsCoppIfPol)
'''
A source relation to the per interface per protocol Control Plane Policing policer.
'''
# Name: The CoPP Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsCoppIfPol_tnCoppIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsCoppIfPol_annotation = ''
# Configure policy:
infraRsCoppIfPol = cobra.model.infra.RsCoppIfPol(infraAccBndlGrp, annotation=infraRsCoppIfPol_annotation, tnCoppIfPolName=infraRsCoppIfPol_tnCoppIfPolName)

# Relation to LLDP Interface Policy (infraRsLldpIfPol)
'''
A source relation to the Link Layer Discovery Protocol policy parameters for the interface.
'''
# Name: The LLDP Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsLldpIfPol_tnLldpIfPolName = 'LLDP_Enabled'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsLldpIfPol_annotation = ''
# Configure policy:
infraRsLldpIfPol = cobra.model.infra.RsLldpIfPol(infraAccBndlGrp, annotation=infraRsLldpIfPol_annotation, tnLldpIfPolName=infraRsLldpIfPol_tnLldpIfPolName)

# Interface Fibre Channel Policy (infraRsFcIfPol) (Relation to Fibre Channel Interface Policy)
'''
A source relation to the Fibre Channel interface policy.
'''
# Name: The Fibre Channel Interface Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsFcIfPol_tnFcIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsFcIfPol_annotation = ''
# Configure policy:
infraRsFcIfPol = cobra.model.infra.RsFcIfPol(infraAccBndlGrp, annotation=infraRsFcIfPol_annotation, tnFcIfPolName=infraRsFcIfPol_tnFcIfPolName)

# Interface Priority Flow Control (infraRsQosPfcIfPol) (Relation to Priority Flow Control Policy)
'''
A source relation to the priority flow control interface policy.
'''
# Name: The Priority Flow Control Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsQosPfcIfPol_tnQosPfcIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsQosPfcIfPol_annotation = ''
# Configure policy:
infraRsQosPfcIfPol = cobra.model.infra.RsQosPfcIfPol(infraAccBndlGrp, annotation=infraRsQosPfcIfPol_annotation, tnQosPfcIfPolName=infraRsQosPfcIfPol_tnQosPfcIfPolName)

# Link Level Policy (fabricHIfPol) (Relation to Link Level Interface Policy)
'''
A source relation to the link level interface policy. The host interface policy specifies the layer 1 parameters of host facing ports.
'''
# Name: The Link Level Policy name. This name can be up to 64 characters. Note that you cannot change this name after the object has been saved.
fabricHIfPol_tnFabricHIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fabricHIfPol_annotation = ''
# Configure policy:
infraRsHIfPol = cobra.model.infra.RsHIfPol(infraAccBndlGrp, annotation=fabricHIfPol_annotation, tnFabricHIfPolName=fabricHIfPol_tnFabricHIfPolName)

# Relation to L2 Port Security Policy (infraRsL2PortSecurityPol)
'''
A source relation to the interface policy providing Layer 2 port security configuration.
'''
# Name: The Port Security Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsL2PortSecurityPol_tnL2PortSecurityPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsL2PortSecurityPol_annotation = ''
# Configure policy:
infraRsL2PortSecurityPol = cobra.model.infra.RsL2PortSecurityPol(infraAccBndlGrp, annotation=infraRsL2PortSecurityPol_annotation, tnL2PortSecurityPolName=infraRsL2PortSecurityPol_tnL2PortSecurityPolName)

# Interface Authentication (802.1x) Policy (infraRsL2PortAuthPol) (Relation to 802.1x Port Authentication Policy)
'''
A source relation to the 802.1x port authentication interface policy.
'''
# Name: The 802.1x Port Authentication Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsL2PortAuthPol_tnL2PortAuthPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsL2PortAuthPol_annotation = ''
# Configure policy:
infraRsL2PortAuthPol = cobra.model.infra.RsL2PortAuthPol(infraAccBndlGrp, annotation=infraRsL2PortAuthPol_annotation, tnL2PortAuthPolName=infraRsL2PortAuthPol_tnL2PortAuthPolName)

# Relation to LACP LAG Policy (infraRsLacpPol)
'''
A source relation to the link aggregation interface policy. This object indicates the LAG policy that is associated with this bundle group.
'''
# Name: The Port Channel Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraRsLacpPol_tnLacpLagPolName = 'LACP_Active'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsLacpPol_annotation = ''
# Configure policy:
infraRsLacpPol = cobra.model.infra.RsLacpPol(infraAccBndlGrp, annotation=infraRsLacpPol_annotation, tnLacpLagPolName=infraRsLacpPol_tnLacpLagPolName)

# Relation to Link Flap Policy (infraRsLinkFlapPol)
'''
A source relation to the link aggregation interface policy. Relationship to policy providing link flap paramateres of the interfaces.
'''
# Name: The Link Flap Policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
# infraRsLinkFlapPol_tnFabricLinkFlapPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
# infraRsLinkFlapPol_annotation = ''
# Configure policy:
# infraRsLinkFlapPol = cobra.model.infra.RsLinkFlapPol(infraAccBndlGrp, annotation=infraRsLinkFlapPol_annotation, tnFabricLinkFlapPolName=infraRsLinkFlapPol_tnFabricLinkFlapPolName)

# ***ATTACHABLE ACCESS ENTITY PROFILE***

# Attachable Access Entity Profile (infraAttEntityP)
'''
The attached entity profile provides a template to deploy hypervisor policies on a large set of leaf ports. 
This also provides the association of a Virtual Machine Management (VMM) domain and the physical network infrastructure.
'''
# Name: The Attached Entity Profile name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
infraAttEntityP_name = 'AEP'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraAttEntityP_annotation = ''
# Description: Specifies a description of the policy definition.
infraAttEntityP_descr = 'Attachable access entity profile.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
infraAttEntityP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
infraAttEntityP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
infraAttEntityP_nameAlias = ''
# Configure policy:
infraAttEntityP = cobra.model.infra.AttEntityP(infraInfra, annotation=infraAttEntityP_annotation, descr=infraAttEntityP_descr, name=infraAttEntityP_name, nameAlias=infraAttEntityP_nameAlias, ownerKey=infraAttEntityP_ownerKey, ownerTag=infraAttEntityP_ownerTag)

# Domain (infraRsDomP)
'''
A source relation to a physical or virtual domain. Users need to create this to provide association between physical infrastructure policies and the domains.
'''
# tDn: The target name of the Domain.
infraRsDomP_tDn = 'uni/phys-Phys_Dom'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsDomP_annotation = ''
# Configure policy:
infraRsDomP = cobra.model.infra.RsDomP(infraAttEntityP, annotation=infraRsDomP_annotation, tDn=infraRsDomP_tDn)

# ***DOMAIN***

# Physical Domain (physDomP)
'''
The physical domain profile stores the physical resources (ports and port-channels) and encap resources (VLAN/VXLAN) that should be used for endpoint groups associated with this domain.
'''
# Name: The name of the Physical Domain. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
physDomP_name = 'Phys_Dom'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
physDomP_annotation = ''
# Owner Key: The key for enabling clients to own their data for entity correlation.
physDomP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
physDomP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
physDomP_nameAlias = ''
# Configure policy:
physDomP = cobra.model.phys.DomP(polUni, annotation=physDomP_annotation, name=physDomP_name, nameAlias=physDomP_nameAlias, ownerKey=physDomP_ownerKey, ownerTag=physDomP_ownerTag)

# Relation to VLAN Pool (infraRsVlanNs)
'''
A source relation to the policy definition for ID ranges used for Virtual Local Area Network encapsulation.
'''
# tDn: The target name of the VLAN Pool associated with the physical domain used for encapsulation. The name of the VLAN Pool is contained in brackets and is followed by the allocation mode (static or dynamic).
infraRsVlanNs_tDn = 'uni/infra/vlanns-[VLAN_Pool]-dynamic'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsVlanNs_annotation = ''
# Configure policy:
infraRsVlanNs = cobra.model.infra.RsVlanNs(physDomP, annotation=infraRsVlanNs_annotation, tDn=infraRsVlanNs_tDn)

# ***VLAN POOL***

# VLAN Pool (fvnsVlanInstP)
'''
The VLAN range namespace policy defines for ID ranges used for VLAN encapsulation.
'''
# Name: The VLAN range namespace policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
fvnsVlanInstP_name = 'VLAN_Pool'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object. 
fvnsVlanInstP_annotation = ''
# Allocation Mode: static or dynamic? Choose one.
fvnsVlanInstP_allocMode = 'dynamic'
# Description: Specifies a description of the policy definition.
fvnsVlanInstP_descr = 'VLAN pool for VLANs 1-4094.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
fvnsVlanInstP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
fvnsVlanInstP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvnsVlanInstP_nameAlias = ''
# Configure policy:
fvnsVlanInstP = cobra.model.fvns.VlanInstP(infraInfra, allocMode=fvnsVlanInstP_allocMode, annotation=fvnsVlanInstP_annotation, descr=fvnsVlanInstP_descr, name=fvnsVlanInstP_name, nameAlias=fvnsVlanInstP_nameAlias, ownerKey=fvnsVlanInstP_ownerKey, ownerTag=fvnsVlanInstP_ownerTag)

# Ranges (fvnsEncapBlk)
'''
The VLAN encapsulation block.
'''
# Name: 
fvnsEncapBlk_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvnsEncapBlk_annotation = ''
# Description: The description of this configuration item.
fvnsEncapBlk_descr = 'VLAN range 1-4094.'
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvnsEncapBlk_nameAlias = ''
# Starting VLAN in range. Choose a VLAN 'vlan-1' - 'vlan-4094':
fvnsEncapBlk_from = 'vlan-1'
# Ending VLAN in range. Choose a VLAN 'vlan-1' - 'vlan-4094':
fvnsEncapBlk_to = 'vlan-4094'
# Allocation Mode: static, dynamic or inherit? Choose one.
fvnsEncapBlk_allocMode = 'static'
# Role: internal or external? Choose one.
fvnsEncapBlk_role = 'external'
# Configure policy:
fvnsEncapBlk = cobra.model.fvns.EncapBlk(fvnsVlanInstP, allocMode=fvnsEncapBlk_allocMode, annotation=fvnsEncapBlk_annotation, descr=fvnsEncapBlk_descr, from_=fvnsEncapBlk_from, name=fvnsEncapBlk_name, nameAlias=fvnsEncapBlk_nameAlias, role=fvnsEncapBlk_role, to=fvnsEncapBlk_to)

# ***VPC EXPLICIT PROTECTION GROUP (VPC DOMAIN)***

# Virtual Port Channel Security Policy (fabricProtPol)
'''
The VPC protection policy is a container of VPC protection groups; it enables you to select a pairing type for creating the protection groups.
'''
# Name: The name of the VPC Protection Policy. This name can be up to 64 characters. Note that you cannot change this name after the object has been saved. The default policy name is 'default'.
fabricProtPol_name = 'default'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fabricProtPol_annotation = ''
# Description: Specifies a description of the policy definition.
fabricProtPol_descr = "vPC security policy."
# Owner Key: The key for enabling clients to own their data for entity correlation.
fabricProtPol_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
fabricProtPol_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fabricProtPol_nameAlias = ''
# Pairing Type: explicit, consecutive or reciprocal? Choose one.
fabricProtPol_pairT = 'explicit'
# Configure policy:
fabricProtPol = cobra.model.fabric.ProtPol(fabricInst, annotation=fabricProtPol_annotation, descr=fabricProtPol_descr, name=fabricProtPol_name, nameAlias=fabricProtPol_nameAlias, ownerKey=fabricProtPol_ownerKey, ownerTag=fabricProtPol_ownerTag, pairT=fabricProtPol_pairT)

# VPC Explicit Protection Group (fabricExplicitGEp)
'''
A VPC explicit protection group represents a VPC domain (a protection group).
You can explicitly configure member nodes of the group using a Fabric policy node endpoint.
'''
# Name: The name of the VPC Explicit Protection Group. This name can be up to 64 characters. Note that you cannot change this name after the object has been saved.
fabricExplicitGEp_name = 'Leaf101_102_VPG'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fabricExplicitGEp_annotation = ''
# ID: Logical Pair ID. Choose a number 1-1000.
fabricExplicitGEp_id = '1'
# Configure policy:
fabricExplicitGEp = cobra.model.fabric.ExplicitGEp(fabricProtPol, annotation=fabricExplicitGEp_annotation, id=fabricExplicitGEp_id, name=fabricExplicitGEp_name)

# Relation to VPC Domain Policy (fabricRsVpcInstPol)
'''
A source relation to the node-level vPC domain policy.
'''
# Name: The name of the VPC Domain Policy. This name can be up to 64 characters. Note that you cannot change this name after the object has been saved. The default policy name is 'default'.
fabricRsVpcInstPol_name = 'default'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fabricRsVpcInstPol_annotation = ''
# Configure policy:
fabricRsVpcInstPol = cobra.model.fabric.RsVpcInstPol(fabricExplicitGEp, annotation=fabricRsVpcInstPol_annotation, tnVpcInstPolName=fabricRsVpcInstPol_name)

# Node Policy End Point (fabricNodePEp)
'''
The node policy endpoint. This is specified by a unique node ID.
'''
# First leaf node in vPC pair.
# Name: The name of the Node Policy End Point. This name can be up to 64 characters. Note that you cannot change this name after the object has been saved. This value is often left blank.
fabricNodePEp_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object. 
fabricNodePEp_annotation = ''
# Description: The description of this configuration item.
fabricNodePEp_descr = 'Node policy endpoint identifier.'
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fabricNodePEp_nameAlias = ''
# ID: Select the node identifier to be added to the vPC pair in the protection group. This is the ID of the leaf node.
fabricNodePEp_id = '102'
# Pod ID: The POD identifier.
fabricNodePEp_podId = '1'
# Configure policy:
fabricNodePEp = cobra.model.fabric.NodePEp(fabricExplicitGEp, annotation=fabricNodePEp_annotation, descr=fabricNodePEp_descr, id=fabricNodePEp_id, name=fabricNodePEp_name, nameAlias=fabricNodePEp_nameAlias, podId=fabricNodePEp_podId)

# Second leaf node in vPC pair.
# Name: The name of the Node Policy End Point. This name can be up to 64 characters. Note that you cannot change this name after the object has been saved. This value is often left blank.
fabricNodePEp2_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object. 
fabricNodePEp2_annotation = ''
# Description: The description of this configuration item.
fabricNodePEp2_descr = 'Node policy endpoint identifier.'
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fabricNodePEp2_nameAlias = ''
# ID: Select the node identifier to be added to the vPC pair in the protection group. This is the ID of the leaf node.
fabricNodePEp2_id = '101'
# Pod ID: The POD identifier.
fabricNodePEp2_podId = '1'
# Configure policy:
fabricNodePEp2 = cobra.model.fabric.NodePEp(fabricExplicitGEp, annotation=fabricNodePEp2_annotation, descr=fabricNodePEp2_descr, id=fabricNodePEp2_id, name=fabricNodePEp2_name, nameAlias=fabricNodePEp2_nameAlias, podId=fabricNodePEp2_podId)

# Commit the generated code to APIC.
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
