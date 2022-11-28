# Basic BGP L3Out policies for connecting an external L3 network to ACI via BGP. Change the variables as needed for your environment. Tested and verified on ACI software version 5.2(5c).

# Imports
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.bgp
import cobra.model.fv
import cobra.model.l3ext
from cobra.internal.codec.xmlcodec import toXMLStr

# Provide login information and establish a connection with the APIC.
ls = cobra.mit.session.LoginSession('https://<apic-ip-address-or-hostname>', '<username>', '<password>')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# ***Top level objects on which operations will be made***

# Distinguished Name: full object name for unique, global identification within the management information tree.
topDn = cobra.mit.naming.Dn.fromString('uni/tn-Tenant/out-BGP_L3Out')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# ***LAYER 3 OUTSIDE***

# L3Out (l3extOut)
'''
The L3 outside policy controls connectivity to the outside.
'''
# Name: The name of the L3Out policy.
l3extOut_name = 'BGP_L3Out'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extOut_annotation = ''
# Description: Specifies a description of the policy definition.
l3extOut_descr = 'BGP L3Out.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
l3extOut_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
l3extOut_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
l3extOut_nameAlias = ''
# Enforce Route Control for Following Directions (the enforce route control type.): import or export?
l3extOut_enforceRtctrl = 'export'
# Out Level DSCP: The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile.
l3extOut_targetDscp = 'unspecified'
# Configure policy:
l3extOut = cobra.model.l3ext.Out(topMo, annotation=l3extOut_annotation, descr=l3extOut_descr, enforceRtctrl=l3extOut_enforceRtctrl, name=l3extOut_name, nameAlias=l3extOut_nameAlias, ownerKey=l3extOut_ownerKey, ownerTag=l3extOut_ownerTag, targetDscp=l3extOut_targetDscp)

# Domain Profile (l3extRsL3DomAtt)
'''
A source relation to the outside domain advertising these prefixes and relationship to the L2 domain for external SVI.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsL3DomAtt_annotation = ''
# tDn: The target name of the external routed domain name.
l3extRsL3DomAtt_tDn = 'uni/l3dom-L3DOM'
# Configure policy:
l3extRsL3DomAtt = cobra.model.l3ext.RsL3DomAtt(l3extOut, annotation=l3extRsL3DomAtt_annotation, tDn=l3extRsL3DomAtt_tDn)

# Private Network (l3extRsEctx)
'''
The private layer 3 network context that belongs to a specific tenant or is shared.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsEctx_annotation = ''
# VRF Target Name: The target name of the relation that defines which private network (layer 3 context or VRF) is associated with the external endpoint group networks (layer 3 instance profile).
l3extRsEctx_tnFvCtxName = 'VRF'
# Configure policy:
l3extRsEctx = cobra.model.l3ext.RsEctx(l3extOut, annotation=l3extRsEctx_annotation, tnFvCtxName=l3extRsEctx_tnFvCtxName)

# Logical Node Profile (l3extLNodeP)
'''
The logical node profile defines a common configuration that can be applied to one or more leaf nodes.
'''
# Name: The name of the logical node profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extLNodeP_name = 'BGP_nodeProfile'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extLNodeP_annotation = ''
# Description: Specifies a description of the policy definition.
l3extLNodeP_descr = 'BGP node profile.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
l3extLNodeP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
l3extLNodeP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
l3extLNodeP_nameAlias = ''
# Tag: Specifies the color of a policy label.
l3extLNodeP_tag = 'yellow-green'
# Target DSCP: The target differentiated service code point (DSCP) of the path attached to the layer 3 outside profile. Specify a value or use the default value of 'unspecified'.
l3extLNodeP_targetDscp = 'unspecified'
# Configure policy:
l3extLNodeP = cobra.model.l3ext.LNodeP(l3extOut, annotation=l3extLNodeP_annotation, descr=l3extLNodeP_descr, name=l3extLNodeP_name, nameAlias=l3extLNodeP_nameAlias, ownerKey=l3extLNodeP_ownerKey, ownerTag=l3extLNodeP_ownerTag, tag=l3extLNodeP_tag, targetDscp=l3extLNodeP_targetDscp)

# Fabric Node (l3extRsNodeL3OutAtt)
'''
A static association with each leaf node that is part of the node profile. The corresponding set of policies will be resolved into the specified node. This object must contain a router ID that will be used as the OSPF/BGP router ID.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsNodeL3OutAtt_annotation = ''
# tDn: The target name of the external routed domain name.
l3extRsNodeL3OutAtt_tDn = 'topology/pod-1/node-101'
# Router ID: The router identifier used as the BGP router ID.
l3extRsNodeL3OutAtt_rtrId = '1.1.1.1'
# Router ID Loopback: is the router-ID address a loopback address? Yes or no?
l3extRsNodeL3OutAtt_rtrIdLoopBack = 'yes'
# Configure policy:
l3extRsNodeL3OutAtt = cobra.model.l3ext.RsNodeL3OutAtt(l3extLNodeP, annotation=l3extRsNodeL3OutAtt_annotation, rtrId=l3extRsNodeL3OutAtt_rtrId, rtrIdLoopBack=l3extRsNodeL3OutAtt_rtrIdLoopBack, tDn=l3extRsNodeL3OutAtt_tDn)

# Infra Logical Node Profile (l3extInfraNodeP)
'''
The infra logical node profile.
'''
# Name: The name of the logical node profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extInfraNodeP_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extInfraNodeP_annotation = ''
# Description: Specifies a description of the policy definition.
l3extInfraNodeP_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
l3extInfraNodeP_nameAlias = ''
# Fabric External Control Peering: Enable/Disable participation of this node in peering for fabric external control traffic. Yes or no?
l3extInfraNodeP_fabricExtCtrlPeering = 'no'
# Fabric External Intersite Control Peering: Enable/Disable participation of this node in peering for intersite control traffic. Yes or no?
l3extInfraNodeP_fabricExtIntersiteCtrlPeering = 'no'
# Spine Role: Spine role played by this node. NULL, inter-pod, msite-forwarder, msite-speaker or wan?
l3extInfraNodeP_spineRole = ''
# Configure policy:
l3extInfraNodeP = cobra.model.l3ext.InfraNodeP(l3extRsNodeL3OutAtt, annotation=l3extInfraNodeP_annotation, descr=l3extInfraNodeP_descr, fabricExtCtrlPeering=l3extInfraNodeP_fabricExtCtrlPeering, fabricExtIntersiteCtrlPeering=l3extInfraNodeP_fabricExtIntersiteCtrlPeering, name=l3extInfraNodeP_name, nameAlias=l3extInfraNodeP_nameAlias, spineRole=l3extInfraNodeP_spineRole)

# Logical Interface Profile (l3extLIfP)
'''
The logical interface profile, which defines a common configuration that can be applied to one or more interfaces.
'''
# Name: The name of the logical node profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extLIfP_name = 'BGP_interfaceProfile'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extLIfP_annotation = ''
# Description: Specifies a description of the policy definition.
l3extLIfP_descr = 'BGP logical interface profile.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
l3extLIfP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
l3extLIfP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
l3extLIfP_nameAlias = ''
# Tag: Specifies the color of a policy label.
l3extLIfP_tag = 'yellow-green'
# Priority: The QoS priority class ID. Options are level1, level2, level3, level4, level5, level6 and unspecified (default value).
l3extLIfP_prio = 'unspecified'
# Configure policy:
l3extLIfP = cobra.model.l3ext.LIfP(l3extLNodeP, annotation=l3extLIfP_annotation, descr=l3extLIfP_descr, name=l3extLIfP_name, nameAlias=l3extLIfP_nameAlias, ownerKey=l3extLIfP_ownerKey, ownerTag=l3extLIfP_ownerTag, prio=l3extLIfP_prio, tag=l3extLIfP_tag)

# Leaf Port (l3extRsPathL3OutAtt)
'''
The path endpoints (ports and port channels) used to reach the external layer 3 network. The corresponding set of policies will be resolved into the specified leaf path endpoints.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsPathL3OutAtt_annotation = ''
# Description: Specifies a description of the policy definition.
l3extRsPathL3OutAtt_desc = ''
# tDn: The target name of the external routed domain name.
l3extRsPathL3OutAtt_tDn = 'topology/pod-1/paths-102/pathep-[eth1/1]'
# Address: The IP address of the path attached to the layer 3 outside profile.
l3extRsPathL3OutAtt_addr = '1.1.1.1/24'
# Autostate: enabled or disabled?
l3extRsPathL3OutAtt_autostate = 'disabled'
# Encap: The encapsulation of the path attached to the layer 3 outside profile.
l3extRsPathL3OutAtt_encap = 'vlan-111'
# Encap Scope: local or ctx (VRF)?
l3extRsPathL3OutAtt_encapScope = 'local'
# Interface Type: External SVI == ext-svi, Routed Interface == l3-port, Routed Sub-Interface == sub-interface, Unspecified == unspecified.
l3extRsPathL3OutAtt_ifInstT = 'ext-svi'
# IPv6 DAD: enabled or disabled?
l3extRsPathL3OutAtt_ipv6Dad = 'enabled'
# Link Layer Address: The override of the system generated IPv6 link-local address.
l3extRsPathL3OutAtt_llAddr = '::'
# MAC Address: The MAC address of the path attached to the layer 3 outside profile.
l3extRsPathL3OutAtt_mac = '00:22:BD:F8:19:FF'
# Mode: The BGP domain mode. Access (802.1P) == native, Trunk == regular, Access (untagged) == untagged.
l3extRsPathL3OutAtt_mode = 'regular'
# MTU: The maximum transmission unit of the external network. Specify a value or use the default value of 'inherit'.
l3extRsPathL3OutAtt_mtu = 'inherit'
# Target DSCP: The target differentiated service code point (DSCP) of the path attached to the layer 3 outside profile. Specify a value or use the default value of 'unspecified'.
l3extRsPathL3OutAtt_targetDscp = 'unspecified'
# Configure policy:
l3extRsPathL3OutAtt = cobra.model.l3ext.RsPathL3OutAtt(l3extLIfP, addr=l3extRsPathL3OutAtt_addr, annotation=l3extRsPathL3OutAtt_annotation, autostate=l3extRsPathL3OutAtt_autostate, descr=l3extRsPathL3OutAtt_desc, encap=l3extRsPathL3OutAtt_encap, encapScope=l3extRsPathL3OutAtt_encapScope, ifInstT=l3extRsPathL3OutAtt_ifInstT, ipv6Dad=l3extRsPathL3OutAtt_ipv6Dad, llAddr=l3extRsPathL3OutAtt_llAddr, mac=l3extRsPathL3OutAtt_mac, mode=l3extRsPathL3OutAtt_mode, mtu=l3extRsPathL3OutAtt_mtu, tDn=l3extRsPathL3OutAtt_tDn, targetDscp=l3extRsPathL3OutAtt_targetDscp)

# Peer Connectivity Profile (bgpPeerP)
'''
The BGP peer connectivity profile contains the peer IP address and defines the peer connectivity control settings. These values are for BGP routers, which can only exchange routing information when they establish a peer connection between them.
'''
# Name: The name of the logical node profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
bgpPeerP_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
bgpPeerP_annotation = ''
# Description: Specifies a description of the policy definition.
bgpPeerP_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
bgpPeerP_nameAlias = ''
# Peer Address: The peer IP address.
bgpPeerP_addr = '1.1.1.2/24'
# Address Type AF Controls: Ucast/Mcast address type AF control. af-label-ucast, af-mcast, or af-ucast?
bgpPeerP_addrTCtrl = 'af-ucast'
# Administrative State: The administrative state of the object or policy. Enabled or disabled?
bgpPeerP_adminSt = 'enabled'
# Allowed Self AS Count: The number of occurrences of a local Autonomous System Number (ASN).
bgpPeerP_allowedSelfAsCnt = '3'
# Peer AF Controls: The peer controls specify which Border Gateway Protocol (BGP) attributes are sent to a peer. Options are allow-self-as, as-override, dis-peer-as-check, nh-self, segment-routing-disable, send-com, and send-ext-com.
bgpPeerP_ctrl = ''
# Peer AF Controls Ext: Peer AF controls ext. Only a single option available, send-domain-path.
bgpPeerP_ctrlExt = ''
# Password: The BGP password.
bgpPeerP_password = ''
# Peer Controls: Bidirectional Forwarding Detection == bfd, Disable checking whether single-hop eBGP peer is directly connected == dis-conn-check.
bgpPeerP_peerCtrl = ''
# Private AS Control: Remove private AS. Options are remove-all, remove-exclusive, and replace-as.
bgpPeerP_privateASctrl = ''
# eBGP Multihop TTL value: Specify the TTL value.
bgpPeerP_ttl = '2'
# Weight: The weight of the fault in calculating the health score of an object. A higher weight causes a higher degradation of the health score of the affected object.
bgpPeerP_weight = '0'
# Configure policy:
bgpPeerP = cobra.model.bgp.PeerP(l3extRsPathL3OutAtt, addr=bgpPeerP_addr, addrTCtrl=bgpPeerP_addrTCtrl, adminSt=bgpPeerP_adminSt, allowedSelfAsCnt=bgpPeerP_allowedSelfAsCnt, annotation=bgpPeerP_annotation, ctrl=bgpPeerP_ctrl, ctrlExt=bgpPeerP_ctrlExt, descr=bgpPeerP_descr, name=bgpPeerP_name, nameAlias=bgpPeerP_nameAlias, password=bgpPeerP_password, peerCtrl=bgpPeerP_peerCtrl, privateASctrl=bgpPeerP_privateASctrl, ttl=bgpPeerP_ttl, weight=bgpPeerP_weight)

# Peer Prefix Policy (bgpRsPeerPfxPol)
'''
The source relation to the peer prefix policy.
'''
# Name: The name of the logical node profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
bgpRsPeerPfxPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
bgpRsPeerPfxPol_annotation = ''
# Configure policy:
bgpRsPeerPfxPol = cobra.model.bgp.RsPeerPfxPol(bgpPeerP, annotation=bgpRsPeerPfxPol_annotation, tnBgpPeerPfxPolName=bgpRsPeerPfxPol_name)

# Local Autonomous System Profile (bgpLocalAsnP)
'''
The local autonomous system information pertaining to a peer.
'''
# Name: The name of the local autonomous system profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
bgpLocalAsnP_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
bgpLocalAsnP_annotation = ''
# Description: Specifies a description of the policy definition.
bgpLocalAsnP_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
bgpLocalAsnP_nameAlias = ''
# ASN Propagation: The local Autonomous System Number (ASN) configuration. dual-as, no-prepend, replace-as, or none?
bgpLocalAsnP_asnPropagate = 'none'
# Local ASN: The local autonomous system number (ASN).
bgpLocalAsnP_localAsn = '65010'
# Configure policy:
bgpLocalAsnP = cobra.model.bgp.LocalAsnP(bgpPeerP, annotation=bgpLocalAsnP_annotation, asnPropagate=bgpLocalAsnP_asnPropagate, descr=bgpLocalAsnP_descr, localAsn=bgpLocalAsnP_localAsn, name=bgpLocalAsnP_name, nameAlias=bgpLocalAsnP_nameAlias)

# Autonomous System Profile (bgpAsP)
'''
The BGP autonomous system profile information.
'''
# Name: The name of the autonomous system profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
bgpAsP_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
bgpAsP_annotation = ''
# Description: Specifies a description of the policy definition.
bgpAsP_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
bgpAsP_nameAlias = ''
# Autonomous System Number: A number that uniquely identifies an autonomous system.
bgpAsP_asn = '65001'
# Configure policy:
bgpAsP = cobra.model.bgp.AsP(bgpPeerP, annotation=bgpAsP_annotation, asn=bgpAsP_asn, descr=bgpAsP_descr, name=bgpAsP_name, nameAlias=bgpAsP_nameAlias)

# ND Policy (l3extRsNdIfPol)
'''
A source relation to an IPv6 neighbor discovery policy.
'''
# Name: The IPv6 neighbor discovery policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extRsNdIfPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsNdIfPol_annotation = ''
# Configure policy:
l3extRsNdIfPol = cobra.model.l3ext.RsNdIfPol(l3extLIfP, annotation=l3extRsNdIfPol_annotation, tnNdIfPolName=l3extRsNdIfPol_name)

# Custom QoS Policy (l3extRsLIfPCustQosPol)
'''
Relationship to custom QoS policy for DSCP to priority mapping.
'''
# Name: The custom QoS policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extRsLIfPCustQosPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsLIfPCustQosPol_annotation = ''
# Configure policy:
l3extRsLIfPCustQosPol = cobra.model.l3ext.RsLIfPCustQosPol(l3extLIfP, annotation=l3extRsLIfPCustQosPol_annotation, tnQosCustomPolName=l3extRsLIfPCustQosPol_name)

# Data Plane Policy Ingress (l3extRsIngressQosDppPol)
'''
Relation to qosDppPol in ingress.
'''
# Name: The data plane policy ingress name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extRsIngressQosDppPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsIngressQosDppPol_annotation = ''
# Configure policy:
l3extRsIngressQosDppPol = cobra.model.l3ext.RsIngressQosDppPol(l3extLIfP, annotation=l3extRsIngressQosDppPol_annotation, tnQosDppPolName=l3extRsIngressQosDppPol_name)

# Data Plane Policy Egress (l3extRsEgressQosDppPol)
'''
Relation to qosDppPol in egress.
'''
# Name: The data plane policy egress name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extRsEgressQosDppPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsEgressQosDppPol_annotation = ''
# Configure policy:
l3extRsEgressQosDppPol = cobra.model.l3ext.RsEgressQosDppPol(l3extLIfP, annotation=l3extRsEgressQosDppPol_annotation, tnQosDppPolName=l3extRsEgressQosDppPol_name)

# ARP Policy (l3extRsArpIfPol)
'''
Relation to ARP policy.
'''
# Name: The ARP policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extRsArpIfPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extRsArpIfPol_annotation = ''
# Configure policy:
l3extRsArpIfPol = cobra.model.l3ext.RsArpIfPol(l3extLIfP, annotation=l3extRsArpIfPol_annotation, tnArpIfPolName=l3extRsArpIfPol_name)

# External Network Instance Profile (l3extInstP)
'''

The external network instance profile represents a group of external subnets that have the same security behavior. These subnets inherit contract profiles applied to the parent instance profile. 
Each subnet can also associate to route control profiles, which defines the routing behavior for that subnet.
'''
# Name: The name of the layer 3 external network instance profile. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extInstP_name = 'BGP_EXT_EPG'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extInstP_annotation = ''
# Description: Specifies a description of the policy definition.
l3extInstP_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
l3extInstP_nameAlias = ''
# Contract Exception Tag:
l3extInstP_exceptionTag = ''
# Flood on Encap: Control at EPG level if the traffic for L2 Multicast/Broadcast and Link Local Layer should be flooded only on ENCAP or based on bridg-domain settings, disabled or enabled?
l3extInstP_floodOnEncap = 'disabled'
# Provider Label Match Criteria: All, AtleastOne, AtmostOne, or None? Default value is AtleastOne.
l3extInstP_matchT = 'AtleastOne'
# Preferred Group Member: Represents parameter used to determine if EPG is part of a group that does not have a contract for communication. Include or exclude?
l3extInstP_prefGrMemb = 'exclude'
# QoS Class: The QoS priority class identifier. level1, level2, level3, level4, level5, level6 or unspecified?
l3extInstP_prio = 'unspecified'
# EPG Level DSCP: The target differentiated services code point (DSCP) of the path attached to the layer 3 outside profile. Default value is unspecified.
l3extInstP_targetDscp = 'unspecified'
# Configure policy:
l3extInstP = cobra.model.l3ext.InstP(l3extOut, annotation=l3extInstP_annotation, descr=l3extInstP_descr, exceptionTag=l3extInstP_exceptionTag, floodOnEncap=l3extInstP_floodOnEncap, matchT=l3extInstP_matchT, name=l3extInstP_name, nameAlias=l3extInstP_nameAlias, prefGrMemb=l3extInstP_prefGrMemb, prio=l3extInstP_prio, targetDscp=l3extInstP_targetDscp)

# Contract Provider (fvRsProv)
'''
A contract for which the EPG will be a provider.
'''
# Contract Name: The provider contract name.
fvRsProv_tnVzBrCPName = 'PERMIT_ICMP'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsProv_annotation = ''
# Install Rules or Estimate Number of Rules: estimate_add, estimate_delete or install? Default value is install.
fvRsProv_intent = 'install'
# Provider Label Match Criteria: All, AtleastOne, AtmostOne, or None? Default value is AtleastOne.
fvRsProv_matchT = 'AtleastOne'
# QoS Class: The QoS priority class identifier. level1, level2, level3, level4, level5, level6 or unspecified?
fvRsProv_prio= 'unspecified'
# Configure policy:
fvRsProv = cobra.model.fv.RsProv(l3extInstP, annotation=fvRsProv_annotation, intent=fvRsProv_intent, matchT=fvRsProv_matchT, prio=fvRsProv_prio, tnVzBrCPName=fvRsProv_tnVzBrCPName)

# Subnet (l3extSubnet)
'''
A subnet for the external Layer 3 network.
'''
# Name: The name of the subnet. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
l3extSubnet_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
l3extSubnet_annotation = ''
# Description: Specifies a description of the policy definition.
l3extSubnet_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
l3extSubnet_nameAlias = ''
# Aggregate Routes for Subnet: export-rtctrl, import-rtctrl, shared-rtctrl or null?
l3extSubnet_aggregate = ''
# Subnet IP Address:
l3extSubnet_ip = '0.0.0.0/0'
# Configure policy:
l3extSubnet = cobra.model.l3ext.Subnet(l3extInstP, aggregate=l3extSubnet_aggregate, annotation=l3extSubnet_annotation, descr=l3extSubnet_descr, ip=l3extSubnet_ip, name=l3extSubnet_name, nameAlias=l3extSubnet_nameAlias)

# Custom QoS Policy (fvRsCustQosPol)
'''
A source relation to a custom QoS policy that enables different levels of service to be assigned to network traffic, including specifications for the Differentiated Services Code Point (DSCP) value(s) and the 802.1p Dot1p priority. This is an internal object.
'''
# Name: The name of the custom QoS traffic policy. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
fvRsCustQosPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsCustQosPol_annotation = ''
# Configure policy:
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(l3extInstP, annotation=fvRsCustQosPol_annotation, tnQosCustomPolName=fvRsCustQosPol_name)

# Contract Consumer (fvRsCons)
'''
The consumer contract profile information.
'''
# Contract Name: The consumer contract name..
fvRsCons_tnVzBrCPName = 'PERMIT_ICMP'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsCons_annotation = ''
# Install Rules or Estimate Number of Rules: estimate_add, estimate_delete or install? Default value is install.
fvRsCons_intent = 'install'
# QoS Class: The QoS priority class identifier. level1, level2, level3, level4, level5, level6 or unspecified?
fvRsCons_prio= 'unspecified'
# Configure policy:
fvRsCons = cobra.model.fv.RsCons(l3extInstP, annotation=fvRsCons_annotation, intent=fvRsCons_intent, prio=fvRsCons_prio, tnVzBrCPName=fvRsCons_tnVzBrCPName)

# External Profile (bgpExtP)
'''
When created, this profile indicates that iBGP will be configured for the endpoint groups in this external network.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
bgpExtP_annotation = ''
# Description: Specifies a description of the policy definition.
bgpExtP_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
bgpExtP_nameAlias = ''
# Configure policy:
bgpExtP = cobra.model.bgp.ExtP(l3extOut, annotation=bgpExtP_annotation, descr=bgpExtP_descr, nameAlias=bgpExtP_nameAlias)

# Commit the generated code to APIC
print(toXMLStr(topMo))
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)
