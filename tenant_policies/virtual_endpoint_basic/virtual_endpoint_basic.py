# Basic tenant policies for connecting a virtual server/host to ACI via VMM integration. Change the variables as needed for your environment. Tested and verified on ACI software version 5.2(5c).

# Imports
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.vmm
import cobra.model.vns
import cobra.model.vz
from cobra.internal.codec.xmlcodec import toXMLStr

# Provide login information and establish a connection with the APIC.
ls = cobra.mit.session.LoginSession('https://<apic-ip-address-or-hostname>', '<username>', '<password>')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# ***Top level objects on which operations will be made***

# Distinguished Name: full object name for unique, global identification within the management information tree.
topDn = cobra.mit.naming.Dn.fromString('uni/tn-Tenant')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# ***TENANT***

# Tenant (fvTenant)
'''
A policy owner in the virtual fabric. A tenant can be either a private or a shared entity. For example, you can create a tenant with contexts and bridge domains shared by other tenants. 
A shared type of tenant is typically named common, default, or infra.
'''
# Name: The name of the tenant.
fvTenant_name = 'Tenant'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvTenant_annotation = ''
# Description: Specifies a description of the policy definition.
fvTenant_descr = 'Tenant for service provider.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
fvTenant_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
fvTenant_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvTenant_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
fvTenant_userdom = 'all'
# Configure policy:
fvTenant = cobra.model.fv.Tenant(topMo, fvTenant_annotation=fvTenant_annotation, descr=fvTenant_descr, name=fvTenant_name, nameAlias=fvTenant_nameAlias, ownerKey=fvTenant_ownerKey, ownerTag=fvTenant_ownerTag, userdom=fvTenant_userdom)

# Service Container (vnsSvcCont)
'''
Service container.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vnsSvcCont_annotation = ''
# User Domain: The AAA domain to which the user belongs.
vnsSvcCont_userdom = 'all'
# Configure policy:
vnsSvcCont = cobra.model.vns.SvcCont(fvTenant, annotation=vnsSvcCont_annotation, userdom=vnsSvcCont_userdom)

# Endpoint Tags Container (fvEpTags)
'''
EP TAGs section.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
# fvEpTags_annotation = ''
# User Domain: The AAA domain to which the user belongs.
# fvEpTags_userdom = 'all'
# Configure policy:
# fvEpTags = cobra.model.fv.EpTags(fvTenant, annotation=fvEpTags_annotation, userdom=fvEpTags_userdom)

# ***VRF***

# Virtual Routing and Forwarding (fvCtx)
'''
The private layer 3 network context that belongs to a specific tenant or is shared.
'''
# Name: The name of the VRF.
fvCtx_name = 'VRF'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvCtx_annotation = ''
# Description: Specifies a description of the policy definition.
fvCtx_descr = 'VRF for service provider tenant.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
fvCtx_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
fvCtx_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvCtx_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
fvCtx_userdom = 'all'
# BD Enforcement Status (BD Enforced Flag): yes or no?
fvCtx_bdEnforcedEnable = 'no'
# IP Data Plane Learning: enabled or disabled?
fvCtx_ipDataPlaneLearning = 'enabled'
# Known Multicast Action: permit or deny?
fvCtx_knwMcastAct = 'permit'
# Policy Enforcement Direction (used for defining policy enforcement direction for the traffic coming to or from an L3Out): ingress or egress?
fvCtx_pcEnfDir = 'ingress'
# Policy Control Enforcement (used to decide whether to enforce or not enforce access control rules for this VRF): enforced or unenforced?
fvCtx_pcEnfPref = 'enforced'
# VRF Index: leave at default value of 0.
fvCtx_vrfIndex = '0'
# Configure policy:
fvCtx = cobra.model.fv.Ctx(fvTenant, annotation=fvCtx_annotation, bdEnforcedEnable=fvCtx_bdEnforcedEnable, descr=fvCtx_descr, ipDataPlaneLearning=fvCtx_ipDataPlaneLearning, knwMcastAct=fvCtx_knwMcastAct, name=fvCtx_name, nameAlias=fvCtx_nameAlias, ownerKey=fvCtx_ownerKey, ownerTag=fvCtx_ownerTag, pcEnfDir=fvCtx_pcEnfDir, pcEnfPref=fvCtx_pcEnfPref, userdom=fvCtx_userdom, vrfIndex=fvCtx_vrfIndex)

# VRF Validation Policy (fvRsVrfValidationPol)
'''
Relationship to the VRF Validation policy
'''
# Name: The name of the VRF validation policy.
fvRsVrfValidationPol_tnL3extVrfValidationPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsVrfValidationPol_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsVrfValidationPol_userdom = 'all'
# Configure policy:
fvRsVrfValidationPol = cobra.model.fv.RsVrfValidationPol(fvCtx, annotation=fvRsVrfValidationPol_annotation, tnL3extVrfValidationPolName=fvRsVrfValidationPol_tnL3extVrfValidationPolName, userdom=fvRsVrfValidationPol_userdom)

# vzAny (vzAny)
'''
vzAny associates all endpoint groups (EPGs) in a context (fvCtx) to one or more contracts (vzBrCP), rather than creating a separate contract relation for each EPG. EPGs can only communicate with other EPGs according to contract rules. 
A relationship between an EPG and a contract specifies whether the EPG provides the communications defined by the contract rules, consumes them, or both. By dynamically applying contract rules to all EPGs in a context, vzAny automates the process of configuring EPG contract relationships. 
Whenever a new EPG is added to a context, vzAny contract rules automatically apply. The vzAny one-to-all EPG relationship is the most efficient way of applying contract rules to all EPGs in a context.
'''
# Name: The name of the vzAny.
vzAny_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vzAny_annotation = ''
# Description: Specifies a description of the policy definition.
vzAny_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
vzAny_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
vzAny_userdom = 'all'
# matchT (Represents the provider label match criteria): All, AtleastOne, AtmostOne or None?
vzAny_matchT = 'AtleastOne'
# Preferred Group Member (Represents parameter used to determine if EPgs can be divided in a the context can be divided in two subgroups.): enabled or disabled?
vzAny_prefGrMemb = 'disabled'
# Configure policy:
vzAny = cobra.model.vz.Any(fvCtx, annotation=vzAny_annotation, descr=vzAny_descr, matchT=vzAny_matchT, name=vzAny_name, nameAlias=vzAny_nameAlias, prefGrMemb=vzAny_prefGrMemb, userdom=vzAny_userdom)

# OSPF Context Policy (fvRsOspfCtxPol)
'''
A source relation to the context-level OSPF timer policy. This is an internal object.
'''
# Name: The name of the OSPF timers policy associated with this context.
fvRsOspfCtxPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsOspfCtxPol_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsOspfCtxPol_userdom = 'all'
# Configure policy:
fvRsOspfCtxPol = cobra.model.fv.RsOspfCtxPol(fvCtx, annotation=fvRsOspfCtxPol_annotation, tnOspfCtxPolName=fvRsOspfCtxPol_name, userdom=fvRsOspfCtxPol_userdom)

# End Point Retention Policy (fvRsCtxToEpRet)
'''
Name of the endpoint retention policy associated with this context.
'''
# Name: The end point retention policy name.
fvRsCtxToEpRet_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
ffvRsCtxToEpRet_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsCtxToEpRet_userdom = 'all'
# Configure policy:
fvRsCtxToEpRet = cobra.model.fv.RsCtxToEpRet(fvCtx, annotation=ffvRsCtxToEpRet_annotation, tnFvEpRetPolName=fvRsCtxToEpRet_name, userdom=fvRsCtxToEpRet_userdom)

# Relationship to External/Transit Route Tag Policy (fvRsCtxToExtRouteTagPol)
'''
The relationship to the external/transit route tag policy.
'''
# Name: The name of the external/transit route tag policy.
fvRsCtxToExtRouteTagPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsCtxToExtRouteTagPol_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsCtxToExtRouteTagPol_userdom = 'all'
# Configure policy:
fvRsCtxToExtRouteTagPol = cobra.model.fv.RsCtxToExtRouteTagPol(fvCtx, annotation=fvRsCtxToExtRouteTagPol_annotation, tnL3extRouteTagPolName=fvRsCtxToExtRouteTagPol_name, userdom=fvRsCtxToExtRouteTagPol_userdom)

# BGP Context Policy (fvRsBgpCtxPol)
'''
A source relation to the BGP timer policy. This is an internal object.
'''
# Name: The name of the BGP timers policy associated with this context.
fvRsBgpCtxPol_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsBgpCtxPol_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsBgpCtxPol_userdom = 'all'
# Configure policy:
fvRsBgpCtxPol = cobra.model.fv.RsBgpCtxPol(fvCtx, annotation=fvRsBgpCtxPol_annotation, tnBgpCtxPolName=fvRsBgpCtxPol_name, userdom=fvRsBgpCtxPol_userdom)

# ***BD***

# Bridge Domain (fvBD)
'''
A bridge domain is a unique layer 2 forwarding domain that contains one or more subnets. Each bridge domain must be linked to a context.
'''
# Name: The name of the BD.
fvBD_name = 'BD'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvBD_annotation = ''
# Description: Specifies a description of the policy definition.
fvBD_descr = 'BD for service provider tenant.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
fvBD_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
fvBD_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvBD_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
fvBD_userdom = 'all'
# ARP Flooding (A property to specify whether ARP flooding is enabled. If flooding is disabled, unicast routing will be performed on the target IP address.): yes or no?
fvBD_arpFlood = 'yes'
# Clear Endpoints (Represents the parameter used by the node (i.e. Leaf) to clear all EPs in all leaves for this BD.): yes or no?
fvBD_epClear = 'no'
# EP Move Detection Mode (The End Point move detection option uses the Gratuitous Address Resolution Protocol (GARP). A gratuitous ARP is an ARP broadcast-type of packet that is used to verify that no other device on the network has the same IP address as the sending device.): garp or null?
fvBD_epMoveDetectMode = ''
# BD Host Based Routing (Enables advertising host routes (/32 prefixes) out of the L3OUT(s) that are associated to this BD.): yes or no?
fvBD_hostBasedRouting = 'no'
# Allow BUM Traffic Between Sites (Allow BUM traffic between sites): yes or no?
fvBD_intersiteBumTrafficAllow = 'no'
# Allow L2Stretch Between Sites: yes or no?
fvBD_intersiteL2Stretch = 'no'
# IP Data Plane Learning: yes or no?
fvBD_ipLearning = 'yes'
# IPv6 Multicast Allow: yes or no?
fvBD_ipv6McastAllow = 'no'
# Limit IP Learning to BD Subnets Only (Limits IP address learning to the bridge domain subnets only. Every BD can have multiple subnets associated with it. By default, all IPs are learned.): yes or no?
fvBD_limitIpLearnToSubnets = 'yes'
# IPv6 Link Local Address (The override of the system generated IPv6 link-local address.): use default value of '::' unless an override is needed.
fvBD_llAddr = '::'
# MAC Address (The MAC address of the bridge domain (BD) or switched virtual interface (SVI). Every BD by default takes the fabric-wide default MAC address. You can override that address with a different one. By default the BD will take a 00:22:BD:F8:19:FF mac address.): use default value of '00:22:BD:F8:19:FF' unless an override is needed.
fvBD_mac = '00:22:BD:F8:19:FF'
# Multicast Allow: yes or no?
fvBD_mcastAllow = 'no'
# Multi Destination Packet Action (The multiple destination forwarding method for L2 Multicast, Broadcast, and Link Layer traffic types.): bd-flood, drop or encap-flood?
fvBD_multiDstPktAct = 'bd-flood'
# Optimize WAN Bandwidth Between Sites: yes or no?
fvBD_OptimizeWanBandwidth = 'no'
# Type (The specific type of the object or component.): regular or fc?
fvBD_type = 'regular'
# Unicast Routing (The forwarding method based on predefined forwarding criteria (IP or MAC address).): yes or no?
fvBD_unicastRoute = 'yes'
# Unknown MAC Unicast Action (The forwarding method for unknown layer 2 destinations.): flood or proxy? 
fvBD_unkMacUcastAct = 'proxy'
# Unknown Multicast Destination Action (The parameter used by the node (i.e. a leaf) for forwarding data for an unknown multicast destination.): flood or opt-flood?
fvBD_unkMcastAct = 'flood'
# Unknown v6 Multicast Destination Action: flood or opt-flood?
fvBD_v6unkMcastAct = 'flood'
# Virtual MAC Address (Virtual MAC address of the BD/SVI. This is used when the BD is extended to multiple sites using l2 Outside.): use default value of 'not-applicable' unless an override is needed.
fvBD_vmac = 'not-applicable'
# Configure policy:
fvBD = cobra.model.fv.BD(fvTenant, OptimizeWanBandwidth=fvBD_OptimizeWanBandwidth, annotation=fvBD_annotation, arpFlood=fvBD_arpFlood, descr=fvBD_descr, epClear=fvBD_epClear, epMoveDetectMode=fvBD_epMoveDetectMode, hostBasedRouting=fvBD_hostBasedRouting, intersiteBumTrafficAllow=fvBD_intersiteBumTrafficAllow, intersiteL2Stretch=fvBD_intersiteL2Stretch, ipLearning=fvBD_ipLearning, ipv6McastAllow=fvBD_ipv6McastAllow, limitIpLearnToSubnets=fvBD_limitIpLearnToSubnets, llAddr=fvBD_llAddr, mac=fvBD_mac, mcastAllow=fvBD_mcastAllow, multiDstPktAct=fvBD_multiDstPktAct, name=fvBD_name, nameAlias=fvBD_nameAlias, ownerKey=fvBD_ownerKey, ownerTag=fvBD_ownerTag, type=fvBD_type, unicastRoute=fvBD_unicastRoute, unkMacUcastAct=fvBD_unkMacUcastAct, unkMcastAct=fvBD_unkMcastAct, userdom=fvBD_userdom, v6unkMcastAct=fvBD_v6unkMcastAct, vmac=fvBD_vmac)

# Subnet (fvSubnet)
'''
A subnet defines the IP address range that can be used within the bridge domain. While a context defines a unique layer 3 space, that space can consist of multiple subnets. These subnets are defined per bridge domain. 
A bridge domain can contain multiple subnets, but a subnet is contained within a single bridge domain.
'''
# Name: The name of the subnet.
fvSubnet_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvSubnet_annotation = ''
# Description: Specifies a description of the policy definition.
fvSubnet_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvSubnet_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
fvSubnet_userdom = 'all'
# Subnet Control State (The control can be specific protocols applied to the subnet such as IGMP Snooping.): nd, no-default-gateway, querier, unspecified or null?
fvSubnet_ctrl = ''
# IP Address: The IP address and mask of the default gateway:
fvSubnet_ip = '192.168.1.1/24'
# IP Data Plane Learning (Knob to disable IP Dataplane Learning for Host(/32, /128) and for BD Subnet): enabled or disabled?
fvSubnet_ipDPLearning = 'enabled'
# Preferred as Primary Subnet (Indicates if the subnet is preferred (primary) over the available alternatives. Only one preferred subnet is allowed.): yes or no?
fvSubnet_preferred = 'yes'
# Treated as Virtual IP Address (Used in case of BD extended to multiple sites): yes or no?
fvSubnet_virtual = 'no'
# Configure policy:
fvSubnet = cobra.model.fv.Subnet(fvBD, annotation=fvSubnet_annotation, ctrl=fvSubnet_ctrl, descr=fvSubnet_descr, ip=fvSubnet_ip, ipDPLearning=fvSubnet_ipDPLearning, name=fvSubnet_name, nameAlias=fvSubnet_nameAlias, preferred=fvSubnet_preferred, userdom=fvSubnet_userdom, virtual=fvSubnet_virtual)

# MLD Snoop Policy (fvRsMldsn)
'''
Relation to a Multicast Listener Discovery (MLD) snoop policy.
'''
# Name: The name of the MLD snoop policy.
fvRsMldsn_tnMldSnoopPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsMldsn_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsMldsn_userdom = 'all'
# Configure policy:
fvRsMldsn = cobra.model.fv.RsMldsn(fvBD, annotation=fvRsMldsn_annotation, tnMldSnoopPolName=fvRsMldsn_tnMldSnoopPolName, userdom=fvRsMldsn_userdom)

# IGMP Snoop Policy (fvRsIgmpsn)
'''
A source relation to the Internet Group Management Protocol (IGMP) snooping policy. This is an internal object.
'''
# Name: The name of the IGMP snoop policy.
fvRsIgmpsn_tnIgmpSnoopPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsIgmpsn_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsIgmpsn_userdom = 'all'
# Configure policy:
fvRsIgmpsn = cobra.model.fv.RsIgmpsn(fvBD, annotation=fvRsIgmpsn_annotation, tnIgmpSnoopPolName=fvRsIgmpsn_tnIgmpSnoopPolName, userdom=fvRsIgmpsn_userdom)

# Private Network (fvRsCtx)
'''
A source relation to a private layer 3 network context that either belongs to a specific tenant or is shared. This is an internal object.
'''
# Name: The name of the associated layer 3 context.
fvRsCtx_tnFvCtxName = 'VRF'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsCtx_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsCtx_userdom = 'all'
# Configure policy:
fvRsCtx = cobra.model.fv.RsCtx(fvBD, annotation=fvRsCtx_annotation, tnFvCtxName=fvRsCtx_tnFvCtxName, userdom=fvRsCtx_userdom)

# End Point Retention Policy (fvRsBdToEpRet)
'''
A source relation to the endpoint retention policy providing the parameters for the lifecycle of the endpoint group. This is an internal object.
'''
# Name: The End Point Retention policy name associated with the bridge domain.
fvRsBdToEpRet_tnFvEpRetPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsBdToEpRet_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsBdToEpRet_userdom = 'all'
# Resolve Action: inherit or resolve? // inherit = Inherit the policy resolved at the logical parent level. Do not resolve the policy here. // resolve = Resolve the policy. // Default value is resolve.
fvRsBdToEpRet_resolveAct = 'resolve'
# Configure policy:
fvRsBdToEpRet = cobra.model.fv.RsBdToEpRet(fvBD, annotation=fvRsBdToEpRet_annotation, resolveAct=fvRsBdToEpRet_resolveAct, tnFvEpRetPolName=fvRsBdToEpRet_tnFvEpRetPolName, userdom=fvRsBdToEpRet_userdom)

# ND Policy (fvRsBDToNdP)
'''
The neighbor discovery policy.
'''
# Name: The name of the ND policy.
fvRsBDToNdP_tnNdIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsBDToNdP_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsBDToNdP_userdom = 'all'
# Configure policy:
fvRsBDToNdP = cobra.model.fv.RsBDToNdP(fvBD, annotation=fvRsBDToNdP_annotation, tnNdIfPolName=fvRsBDToNdP_tnNdIfPolName, userdom=fvRsBDToNdP_userdom)

# Monitoring Policy (fvRsTenantMonPol)
'''
A source relation to the monitoring policy model for the endpoint group semantic scope. This is an internal object.
'''
# Name: The monitoring policy name for the EPG semantic scope.
fvRsTenantMonPol_tnMonEPGPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsTenantMonPol_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsTenantMonPol_userdom = 'all'
# Configure policy:
fvRsTenantMonPol = cobra.model.fv.RsTenantMonPol(fvTenant, annotation=fvRsTenantMonPol_annotation, tnMonEPGPolName=fvRsTenantMonPol_tnMonEPGPolName, userdom=fvRsTenantMonPol_userdom)

# ***AP***

# Application Profile (fvAp)
'''
The application profile is a set of requirements that an application instance has on the virtualizable fabric. The policy regulates connectivity and visibility among endpoints within the scope of the policy.
'''
# Name: The name of the AP.
fvAp_name = 'AP'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvAp_annotation = ''
# Description: Specifies a description of the policy definition.
fvAp_descr = 'AP for service provider tenant.'
# Owner Key: The key for enabling clients to own their data for entity correlation.
fvAp_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
fvAp_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvAp_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
fvAp_userdom = 'all'
# Priority (The priority class identifier, aka QoS class): level1, level2, level3, level4, level5, level6, or unspecified? Default value is unspecified.
fvAp_prio = 'unspecified'
# Configure policy:
fvAp = cobra.model.fv.Ap(fvTenant, annotation=fvAp_annotation, descr=fvAp_descr, name=fvAp_name, nameAlias=fvAp_nameAlias, ownerKey=fvAp_ownerKey, ownerTag=fvAp_ownerTag, prio=fvAp_prio, userdom=fvAp_userdom)

# ***EPG***

# Application EPG (fvAEPg)
'''
A set of requirements for the application-level EPG instance. The policy regulates connectivity and visibility among the end points within the scope of the policy.
'''
# Name: The name of the EPG.
fvAEPg_name = 'VM_EPG'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvAEPg_annotation = ''
# Description: Specifies a description of the policy definition.
fvAEPg_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
fvAEPg_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
fvAEPg_userdom = 'all'
# Contract Exception Tag: A custom tag for contract exceptions.
fvAEPg_exceptionTag = ''
# Handling of L2 Multicast/Broadcast and Link-Layer traffic at EPG level (Control at EPG level if the traffic L2 Multicast/Broadcast and Link Local Layer should be flooded only on ENCAP or based on bridge-domain settings): enabled or disabled?
fvAEPg_floodOnEncap = 'disabled'
# Forwarding Control Bits (Forwarding control): proxy-arp or null?
fvAEPg_fwdCtrl = ''
# EPG with Multisite Mcast Source: yes or no?
fvAEPg_hasMcastSource = 'no'
# Attribute Based EPG: yes or no?
fvAEPg_isAttrBasedEPg = 'no'
# Provider Label Match Criteria (The provider label match criteria.): All, AtleastOne, AtmostOne or None?
fvAEPg_matchT = 'AtleastOne'
# Policy Control Enforcement (The preferred policy control.): enforced or unenforced?
fvAEPg_pcEnfPref = 'unenforced'
# Preferred Group Member (Represents parameter used to determine if EPg is part of a group that does not a contract for communication): include or exclude?
fvAEPg_prefGrMemb = 'exclude'
# QoS Class (The QoS priority class identifier.): level1, level2, level3, level4, level5, level6, or unspecified? Default value is unspecified.
fvAEPg_prio = 'unspecified'
# Withdraw AEPg Configuration from all Nodes in the Fabric: yes or no?
fvAEPg_shutdown = 'no'
# Configure policy:
fvAEPg = cobra.model.fv.AEPg(fvAp, annotation=fvAEPg_annotation, descr=fvAEPg_descr, exceptionTag=fvAEPg_exceptionTag, floodOnEncap=fvAEPg_floodOnEncap, fwdCtrl=fvAEPg_fwdCtrl, hasMcastSource=fvAEPg_hasMcastSource, isAttrBasedEPg=fvAEPg_isAttrBasedEPg, matchT=fvAEPg_matchT, name=fvAEPg_name, nameAlias=fvAEPg_nameAlias, pcEnfPref=fvAEPg_pcEnfPref, prefGrMemb=fvAEPg_prefGrMemb, prio=fvAEPg_prio, shutdown=fvAEPg_shutdown, userdom=fvAEPg_userdom)

# Domain
'''
An EPG can be linked to a domain profile via the Associated Domain Profiles. The domain profiles attached can be VMM, Physical, L2 External, or L3 External Domains.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsDomAtt_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsDomAtt_userdom = 'all'
# Encap: The port encapsulation (default value is 'unknown').
fvRsDomAtt_encap = 'vlan-2'
# Deployment Immediacy (Once policies are downloaded to the leaf software, deployment immediacy can specify when the policy is pushed into the hardware policy CAM.): immediate or lazy? (lazy = On Demand)
fvRsDomAtt__instrImedcy = 'immediate'
# Encap Mode: vlan, vxlan or auto?
ffvRsDomAtt_encapMode = 'auto'
# Primary Encap: If the application EPG requires a primary VLAN, enter the primary VLAN here.
fvRsDomAtt_primaryEncap = 'unknown'
# Primary Encap Inner: the primary inner encap (default value is 'unknown').
fvRsDomAtt_primaryEncapInner = 'unknown'
# Secondary Encap Inner: the secondary inner encap (default value is 'unknown').
fvRsDomAtt_secondaryEncapInner = 'unknown'
# tDn: The target name of the physical domain profile.
fvRsDomAtt_tDn = 'uni/vmmp-VMware/dom-VMM'
# Binding Type: dynamicBinding, ephemeral, staticBinding or none?
fvRsDomAtt_bindingType = 'staticBinding'
# Class Preference: encap or useg?
fvRsDomAtt_classPref = 'encap'
# Custom EPG Name: define a custom EPG name if desired.
fvRsDomAtt_customEpgName = ''
# Delimeter: define a delimeter if desired. Regex ^[^a-zA-Z0-9;>"-*`,-.;\[\]/\\{}:?\s&<]+$.
fvRsDomAtt_delimiter = ''
# EPG CoS (define the class of service value.): Cos0, Cos1, Cos2, Cos3, Cos4, Cos5, Cos6 or Cos7?
fvRsDomAtt_epgCos = 'Cos0'
# EPG Cos Preference: enabled or disabled?
fvRsDomAtt_epgCosPref = 'disabled'
# LAG Policy Name: the name of the LAG policy.
fvRsDomAtt_lagPolicyName = ''
# Netflow Direction: ingress, egress or both?
fvRsDomAtt_netflowDir = 'both'
# Netflow Preference: enabled or disabled?
fvRsDomAtt_netflowPref = 'disabled'
# Number of Ports: The number of ports existing operationally in the module (default value is 0).
fvRsDomAtt_numPorts = '8'
# Port Allocation: elastic, fixed or none?
fvRsDomAtt_portAllocation = 'fixed'
# Resolution Immediacy: specifies if policies are to be resolved immmediately or when needed.
fvRsDomAtt_resImedcy = 'pre-provision'
# Switching Mode: AVE or native?
fvRsDomAtt_switchingMode = 'native'
# Untagged: yes or no?
fvRsDomAtt_untagged = 'no'
# VNet Only: yes or no?
fvRsDomAtt_vnetOnly = 'no'
# Configure policy:
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, annotation='', bindingType=fvRsDomAtt_bindingType, classPref=fvRsDomAtt_classPref, customEpgName=fvRsDomAtt_customEpgName, delimiter=fvRsDomAtt_delimiter, encap=fvRsDomAtt_encap, encapMode=ffvRsDomAtt_encapMode, epgCos=fvRsDomAtt_epgCos, epgCosPref=fvRsDomAtt_epgCosPref, instrImedcy=fvRsDomAtt__instrImedcy, lagPolicyName=fvRsDomAtt_lagPolicyName, netflowDir=fvRsDomAtt_netflowDir, netflowPref=fvRsDomAtt_netflowPref, numPorts=fvRsDomAtt_numPorts, portAllocation=fvRsDomAtt_portAllocation, primaryEncap=fvRsDomAtt_primaryEncap, primaryEncapInner=fvRsDomAtt_primaryEncapInner, resImedcy=fvRsDomAtt_resImedcy, secondaryEncapInner=fvRsDomAtt_secondaryEncapInner, switchingMode=fvRsDomAtt_switchingMode, tDn=fvRsDomAtt_tDn, untagged=fvRsDomAtt_untagged, userdom=fvRsDomAtt_userdom, vnetOnly=fvRsDomAtt_vnetOnly)

# VMM Security Policy
'''
Security policy for the VMM integration.
'''
# Name: The name of the VMM security policy.
vmmSecP_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmSecP_annotation = ''
# Description: Specifies a description of the policy definition.
vmmSecP_descr = ''
# Owner Key: The key for enabling clients to own their data for entity correlation.
vmmSecP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
vmmSecP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
vmmSecP_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
vmmSecP_userdom = 'all'
# Promiscuous Mode: accept or reject? Default is reject.
vmmSecP_allowPromiscuous = 'reject'
# Forged Transmits: accept or reject? Default is reject.
vmmSecP_forgedTransmits = 'reject'
# MAC Address Changes: accept or reject? Default is reject.
vmmSecP_macChanges = 'reject'
# Configure policy:
vmmSecP = cobra.model.vmm.SecP(fvRsDomAtt, allowPromiscuous=vmmSecP_allowPromiscuous, annotation=vmmSecP_annotation, descr=vmmSecP_descr, forgedTransmits=vmmSecP_forgedTransmits, macChanges=vmmSecP_macChanges, name=vmmSecP_name, nameAlias=vmmSecP_nameAlias, ownerKey=vmmSecP_ownerKey, ownerTag=vmmSecP_ownerTag, userdom=vmmSecP_userdom)

# Custom QoS Policy (fvRsCustQosPol)
'''
A source relation to a custom QoS policy that enables different levels of service to be assigned to network traffic, including specifications for the Differentiated Services Code Point (DSCP) value(s) and the 802.1p Dot1p priority. This is an internal object.
'''
# Name: The name of the custom QoS policy.
fvRsCustQosPol_tnQosCustomPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsCustQosPol_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsCustQosPol_userdom = 'all'
# Configure policy:
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, annotation=fvRsCustQosPol_annotation, tnQosCustomPolName=fvRsCustQosPol_tnQosCustomPolName, userdom=fvRsCustQosPol_userdom)

# Bridge Domain for the EPG (fvRsBd)
'''
A source relation to the bridge domain associated to this endpoint group. This is an internal object.
'''
# Name: The name of the bridge domain related to this EPG.
fvRsBd_tnFvBDName = 'BD'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
fvRsBd_annotation = ''
# User Domain: The AAA domain to which the user belongs.
fvRsBd_userdom = 'all'
# Configure policy:
fvRsBd = cobra.model.fv.RsBd(fvAEPg, annotation=fvRsBd_annotation, tnFvBDName=fvRsBd_tnFvBDName, userdom=fvRsBd_userdom)

# Commit the generated code to APIC
print(toXMLStr(topMo))
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)