# VMware VMM integration policies for connecting vCenter to ACI. Change the variables as needed for your environment. Tested and verified on ACI software version 5.2(5c).

# Imports
import cobra.mit.access
import cobra.mit.naming
import cobra.mit.request
import cobra.mit.session
import cobra.model.infra
import cobra.model.pol
import cobra.model.vmm
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
# Distinguished Name: full object name for unique, global identification within the management information tree.
topDn = cobra.mit.naming.Dn.fromString('uni/vmmp-VMware/dom-VMM')
topParentDn = topDn.getParent()
topMo = md.lookupByDn(topParentDn)

# ***ASSOCIATED ATTACHABLE ENTITY PROFILE***

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
infraRsDomP_tDn = 'uni/vmmp-VMware/dom-VMM'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsDomP_annotation = ''
# Configure policy:
infraRsDomP = cobra.model.infra.RsDomP(infraAttEntityP, annotation=infraRsDomP_annotation, tDn=infraRsDomP_tDn)

# ***VMM DOMAIN***

# VMM Domain (vmmDomP)
'''
The VMM domain profile is a policy for grouping VM controllers with similar networking policy requirements. For example, the VM controllers can share VLAN or VXLAN space and application endpoint groups. The APIC communicates with the controller to publish network configurations such as port groups that are then applied to the virtual workloads.
'''
# Name: The name of the VMM domain.
vmmDomP_name = 'VMM'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmDomP_annotation = ''
# Owner Key: The key for enabling clients to own their data for entity correlation.
vmmDomP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
vmmDomP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
vmmDomP_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
vmmDomP_userdom = 'all'
# Access Mode: read-only or read-write?
vmmDomP_accessMode = 'read-write'
# ARP Learning (Enable/Disable ARP learning for AVS Domain): enabled, disabled or null?
vmmDomP_arpLearning = ''
# AVE Timeout (The time period in seconds without a Cisco ACI Virtual Edge heartbeat. After this time period, Cisco Application Policy Infrastructure Controller (APIC) notifies VMware vCenter that Cisco ACI Virtual Edge has stopped working. VMware vCenter eventually quarantines any host where Cisco ACI Virtual Edge stops working.): Choose a value between 10-300.
vmmDomP_aveTimeOut = '30'
# Configure Infra Port Groups (Configure port groups for Virtual APIC for Cisco ACI Virtual Edge and VMware VDS only): yes or no?
vmmDomP_configInfraPg = 'no'
# Control Knob (Determines whether to turn on EP datapath verify or not.): epDpVerify or none?
vmmDomP_ctrlKnob = 'epDpVerify'
# Delimiter: The delimiter optionally chosen during vCenter domain creation. You can choose a symbol to use as the delimiter in the VMware portgroup name. If you do not choose a delimiter, the system uses the default | (pipe) delimiter.
vmmDomP_delimiter = ''
# Enable AVE: yes or no?
vmmDomP_enableAVE = 'no'
# Enable Tag Collection (Checking the check box enables Cisco APIC to collect VMs that have been assigned tags in VMware vCenter for microsegmentation. This option is available for Cisco ACI Virtual Edge and VMware VDS.): yes or no?
vmmDomP_enableTag = 'no'
# Enable VM Folder Data Retrieval: yes or no?
vmmDomP_enableVmFolder = 'no'
# Encap Mode: vlan, vxlan, ivxlan or unknown?
vmmDomP_encapMode = 'unknown'
# Switching Preference (The switching enforcement preference. This determines whether switches can be done within the virtual switch (Local Switching) or whether all switched traffic must go through the fabric (No Local Switching).): hw, sw or unknown?
vmmDomP_enfPref = 'hw'
# EP Inventory Type (on-link = Inventory contains all endpoints that share a fabric uplink // none = No endpoints should be included in the inventory): on-link or none?
vmmDomP_epInventoryType = 'on-link'
# End Point Retention Time: The number of seconds an endpoint is retained after it has been marked for deletion. You can choose from 0 seconds to 600 seconds. The default is 0 seconds.
vmmDomP_epRetTime = '0'
# Enable Host Availability Monitoring (creates a VMware Proactive HA provider object in VMware vCenter. The object enables you to quarantine a host on which Cisco ACI Virtual Edge has stopped working. The VMware vCenter also moves any virtual machines (VMs) from the host to hosts where Cisco ACI Virtual Edge is working.): yes or no?
vmmDomP_hvAvailMonitor = 'no'
# Multicast Address: The multicast address of the VMM domain profile.
vmmDomP_mcastAddr = '0.0.0.0'
# Virtual Switch Mode (The switch to be used for the domain profile // cf = Cloud Foundry // default = Distributed Switch (VDS/DVS) // k8s = Kubernetes // n1kv = Cisco AVS // nsx = NSX // openshift = OpenShift // ovs = Open vSwitch // rancher = Rancher RKE // rhev = RHEV): cf, default, k8s, n1kv, nsx, openshift, ovs, rancher, rhev or unknown?
vmmDomP_mode = 'default'
# Default Encap Mode (The default encapsulation mode for the Cisco AVS VMM domain. Depending on the mode you choose, you might need to configure a VLAN or multicast pool.): unspecified, vlan or vxlan?
vmmDomP_prefEncapMode = 'unspecified'
# Configure policy:
vmmDomP = cobra.model.vmm.DomP(topMo, accessMode=vmmDomP_accessMode, annotation=vmmDomP_annotation, arpLearning=vmmDomP_arpLearning, aveTimeOut=vmmDomP_aveTimeOut, configInfraPg=vmmDomP_configInfraPg, ctrlKnob=vmmDomP_ctrlKnob, delimiter=vmmDomP_delimiter, enableAVE=vmmDomP_enableAVE, enableTag=vmmDomP_enableTag, enableVmFolder=vmmDomP_enableVmFolder, encapMode=vmmDomP_encapMode, enfPref=vmmDomP_enfPref, epInventoryType=vmmDomP_epInventoryType, epRetTime=vmmDomP_epRetTime, hvAvailMonitor=vmmDomP_hvAvailMonitor, mcastAddr=vmmDomP_mcastAddr, mode=vmmDomP_mode, name=vmmDomP_name, nameAlias=vmmDomP_nameAlias, ownerKey=vmmDomP_ownerKey, ownerTag=vmmDomP_ownerTag, prefEncapMode=vmmDomP_prefEncapMode, userdom=vmmDomP_userdom)

# Relation to VLAN Pool (infraRsVlanNs)
'''
A source relation to the policy definition for ID ranges used for VLAN encapsulation.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
infraRsVlanNs_annotation = ''
# tDn: The target name of the VLAN pool associated with the physical domain used for encapsulation.
infraRsVlanNs_tDn = 'uni/infra/vlanns-[VLAN_Pool]-dynamic'
# Configure policy:
infraRsVlanNs = cobra.model.infra.RsVlanNs(vmmDomP, annotation=infraRsVlanNs_annotation, tDn=infraRsVlanNs_tDn)

# LLDP Interface Policy (vmmRsDefaultLldpIfPol)
'''
A source relation to the LLDP policy parameters for the interface.
'''
# Name: The name of the LLDP interface policy.
vmmRsDefaultLldpIfPol_tnLldpIfPolName = 'LLDP_Enabled'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsDefaultLldpIfPol_annotation = ''
# Configure policy:
vmmRsDefaultLldpIfPol = cobra.model.vmm.RsDefaultLldpIfPol(vmmDomP, annotation=vmmRsDefaultLldpIfPol_annotation, tnLldpIfPolName=vmmRsDefaultLldpIfPol_tnLldpIfPolName)

# CDP Interface Policy (vmmRsDefaultCdpIfPol)
'''
A source relation to the Cisco Discovery Channel interface policy.
'''
# Name: The name of the CDP interface policy.
vmmRsDefaultCdpIfPol_tnCdpIfPolName = 'CDP_Enabled'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsDefaultCdpIfPol_annotation = ''
# Configure policy:
vmmRsDefaultCdpIfPol = cobra.model.vmm.RsDefaultCdpIfPol(vmmDomP, annotation=vmmRsDefaultCdpIfPol_annotation, tnCdpIfPolName=vmmRsDefaultCdpIfPol_tnCdpIfPolName)

# VMM Controller (vmmCtrlrP)
'''
The VMM controller profile specifies how to connect to a single VM management controller that is part of a policy enforcement domain. For example, the VMM controller profile could be a policy to connect a VMware vCenter that is part of a VMM domain.
'''
# Name: The name of the VMM controller.
vmmCtrlrP_name = 'vCenter'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmCtrlrP_annotation = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
vmmCtrlrP_nameAlias = ''
# User Domain: The AAA domain to which the user belongs.
vmmCtrlrP_userdom = 'all'
# DVS Version (The DVS version. The default is vCenter Default. (unmanaged = vCenter Default): unmanaged, 5.1, 5.5, 6.0, 6.5, 6.6 or 7.0?
vmmCtrlrP_dvsVersion = 'unmanaged'
# Hostname or IP Address: The hostname or IP address.
vmmCtrlrP_hostOrIp = '192.168.1.1'
# Triggered Inventory Sync Status (The default value is untriggered.): triggered, untriggered or autoTriggered?
vmmCtrlrP_inventoryTrigSt = 'untriggered'
# Mode: cf = Cloud Foundry // default = Distributed Switch (VDS/DVS) // k8s = Kubernetes // n1kv = Cisco AVS // nsx = NSX // openshift = OpenShift // ovs = Open vSwitch // rancher = Rancher RKE // rhev = RHEV): cf, default, k8s, n1kv, nsx, openshift, ovs, rancher, rhev or unknown?
vmmCtrlrP_mode = 'default'
# Deployment Error Message of Microsoft Plugin SCVMM Controller (for SCVMM only): captures error message encountered in SCVMM Controller plugin. This error message represents specific details for bitmask based msftConfigIssues fault.
vmmCtrlrP_msftConfigErrMsg = ''
# SCVMM Controller Conguration Issues Error Message (for SCVMM only, the default value is not-applicable.): not-applicable, invalid-rootContName, duplicate-rootContName, missing-hostGroup-in-cloud, missing-rootContName, aaacert-invalid, inventory-failed, invalid-object-in-inventory, duplicate-mac-in-inventory or zero-mac-in-inventory?
vmmCtrlrP_msftConfigIssues = ''
# Cisco AVS Statistics Mode (for AVS only, the default value is enabled.): 
#vmmCtrlrP_n1kvStatsMode = ''
# Port: use the default value of 0.
vmmCtrlrP_port = '0'
# Datacenter: the top-level container (DC) name. This must match the Datacenter name on vCenter that you want to connect to.
vmmCtrlrP_rootContName = 'DC'
# Sequence Number: An ISIS link-state packet sequence number (Use the default value of 0).
vmmCtrlrP_seqNum = '0'
# Statistics Mode (collect statistics from controller): enabled, disabled or unknown?
vmmCtrlrP_statsMode = 'disabled'
# VxLAN Deployment Preference: vxlan or nsx?
vmmCtrlrP_vxlanDeplPref = 'vxlan'
# Configure policy:
vmmCtrlrP = cobra.model.vmm.CtrlrP(vmmDomP, annotation=vmmCtrlrP_annotation, dvsVersion=vmmCtrlrP_dvsVersion, hostOrIp=vmmCtrlrP_hostOrIp, inventoryTrigSt=vmmCtrlrP_inventoryTrigSt, mode=vmmCtrlrP_mode, msftConfigErrMsg=vmmCtrlrP_msftConfigErrMsg, msftConfigIssues=vmmCtrlrP_msftConfigIssues, name=vmmCtrlrP_name, nameAlias=vmmCtrlrP_nameAlias, port=vmmCtrlrP_port, rootContName=vmmCtrlrP_rootContName, seqNum=vmmCtrlrP_seqNum, statsMode=vmmCtrlrP_statsMode, vxlanDeplPref=vmmCtrlrP_vxlanDeplPref, userdom=vmmCtrlrP_userdom)
#n1kvStatsMode=vmmCtrlrP_n1kvStatsMode, not using this right now.

# User Access Profile (vmmRsAcc)
'''
A source relation to the user account profile.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsAcc_annotation = ''
# tDn: The target name of the account profile policy for VMM controller.
vmmRsAcc_tDn = 'uni/vmmp-VMware/dom-VMM/usracc-vCenter-Creds'
# Configure policy:
vmmRsAcc = cobra.model.vmm.RsAcc(vmmCtrlrP, annotation=vmmRsAcc_annotation, tDn=vmmRsAcc_tDn)

# Firewall Policy (vmmRsDefaultFwPol)
'''
A source relation to the Firewall interface policy.
'''
# Name: The Firewall policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
vmmRsDefaultFwPol_tnNwsFwPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsDefaultFwPol_annotation = ''
# Configure policy:
vmmRsDefaultFwPol = cobra.model.vmm.RsDefaultFwPol(vmmDomP, annotation=vmmRsDefaultFwPol_annotation, tnNwsFwPolName=vmmRsDefaultFwPol_tnNwsFwPolName)

# LACP Policy (vmmRsDefaultLacpLagPol)
'''
A source relation to the link aggregation interface policy.
'''
# Name: The link aggregation policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
vmmRsDefaultLacpLagPol_tnLacpLagPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsDefaultLacpLagPol_annotation = ''
# Configure policy:
vmmRsDefaultLacpLagPol = cobra.model.vmm.RsDefaultLacpLagPol(vmmDomP, annotation=vmmRsDefaultLacpLagPol_annotation, tnLacpLagPolName=vmmRsDefaultLacpLagPol_tnLacpLagPolName)

# VSwitch Policy Group (vmmVSwitchPolicyCont)
'''
VSwitch Policy Group. Container for the vswitch policies.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmVSwitchPolicyCont_annotation = ''
# Description: Specifies a description of the policy definition.
vmmVSwitchPolicyCont_descr = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
vmmVSwitchPolicyCont_nameAlias = ''
# Configure policy:
vmmVSwitchPolicyCont = cobra.model.vmm.VSwitchPolicyCont(vmmDomP, annotation=vmmVSwitchPolicyCont_annotation, descr=vmmVSwitchPolicyCont_descr, nameAlias=vmmVSwitchPolicyCont_nameAlias)

# Relation to MTU Policy (vmmRsVswitchOverrideMtuPol)
'''
Relationship to policy providing physical configuration of the interfaces.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
'''vmmRsVswitchOverrideMtuPol_annotation = ''
# tDn: The target name of the MTU policy.
vmmRsVswitchOverrideMtuPol_tDn = 'uni/fabric/l2pol-default'
# Configure policy:
vmmRsVswitchOverrideMtuPol = cobra.model.vmm.RsVswitchOverrideMtuPol(vmmVSwitchPolicyCont, annotation=vmmRsVswitchOverrideMtuPol_annotation, tDn=vmmRsVswitchOverrideMtuPol_tDn)'''

# Relation to LLDP Interface Policy (vmmRsVswitchOverrideLldpIfPol)
'''
A source relation to the link layer discovery protocol interface policy.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsVswitchOverrideLldpIfPol_annotation = ''
# tDn: The target name of the LLDP policy.
vmmRsVswitchOverrideLldpIfPol_tDn = 'uni/infra/lldpIfP-LLDP_Enabled'
# Configure policy:
vmmRsVswitchOverrideLldpIfPol = cobra.model.vmm.RsVswitchOverrideLldpIfPol(vmmVSwitchPolicyCont, annotation=vmmRsVswitchOverrideLldpIfPol_annotation, tDn=vmmRsVswitchOverrideLldpIfPol_tDn)

# Relation to LACP Lag Policy (vmmRsVswitchOverrideLacpPol)
'''
A source relation to the LACP Lag Policy.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsVswitchOverrideLacpPol_annotation = ''
# tDn: The target name of the LACP policy.
vmmRsVswitchOverrideLacpPol_tDn = 'uni/infra/lacplagp-MAC_Pinning'
# Configure policy:
vmmRsVswitchOverrideLacpPol = cobra.model.vmm.RsVswitchOverrideLacpPol(vmmVSwitchPolicyCont, annotation=vmmRsVswitchOverrideLacpPol_annotation, tDn=vmmRsVswitchOverrideLacpPol_tDn)

# Relation to CDP Interface Policy (vmmRsVswitchOverrideCdpIfPol)
'''
A source relation the the Cisco discovery protocol interface policy.
'''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsVswitchOverrideCdpIfPol_annotation = ''
# tDn: The target name of the CDP policy.
vmmRsVswitchOverrideCdpIfPol_tDn = 'uni/infra/cdpIfP-CDP_Enabled'
# Configure policy:
vmmRsVswitchOverrideCdpIfPol = cobra.model.vmm.RsVswitchOverrideCdpIfPol(vmmVSwitchPolicyCont, annotation=vmmRsVswitchOverrideCdpIfPol_annotation, tDn=vmmRsVswitchOverrideCdpIfPol_tDn)

# STP Interface Policy (vmmRsDefaultStpIfPol)
'''
A source relation to the spanning-tree protocol interface policy.
'''
# Name: The STP policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
vmmRsDefaultStpIfPol_tnStpIfPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vvmmRsDefaultStpIfPol_annotation = ''
# Configure policy:
vmmRsDefaultStpIfPol = cobra.model.vmm.RsDefaultStpIfPol(vmmDomP, annotation=vvmmRsDefaultStpIfPol_annotation, tnStpIfPolName=vmmRsDefaultStpIfPol_tnStpIfPolName)

# Uplink Policy Container (vmmUplinkPCont)
'''
Object to create uplinks for the virtual switch uplink port group.
'''
# Name: The uplink name.
vmmUplinkPCont_name = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmUplinkPCont_annotation = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
vmmUplinkPCont_nameAlias = ''
# Uplink ID:
vmmUplinkPCont_id = '0'
# Number of Uplinks:
vmmUplinkPCont_numOfUplinks = '8'
# Configure policy:
vmmUplinkPCont = cobra.model.vmm.UplinkPCont(vmmDomP, annotation=vmmUplinkPCont_annotation, id=vmmUplinkPCont_id, name=vmmUplinkPCont_name, nameAlias=vmmUplinkPCont_nameAlias, numOfUplinks=vmmUplinkPCont_numOfUplinks)

# L2 Instance Policy (vmmRsDefaultL2InstPol)
'''
A source relation to the Layer 2 instance policy information.
'''
# Name: The L2 instance policy name. This name can be up to 64 alphanumeric characters. Note that you cannot change this name after the object has been saved.
vmmRsDefaultL2InstPol_tnL2InstPolName = ''
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmRsDefaultL2InstPol_annotation = ''
# Configure policy:
vmmRsDefaultL2InstPol = cobra.model.vmm.RsDefaultL2InstPol(vmmDomP, annotation=vmmRsDefaultL2InstPol_annotation, tnL2InstPolName=vmmRsDefaultL2InstPol_tnL2InstPolName)

# VMM Credential (vmmUsrAccP)
'''
The user account profile that is used to access a VM provider account.
'''
# Name: The name of the VMM credential policy.
vvmmUsrAccP_name = 'vCenter-Creds'
# Annotation: An annotation for enabling clients to add arbitrary key:value pairs of metadata to an object.
vmmUsrAccP_annotation = ''
# Description: Specifies a description of the policy definition.
vmmUsrAccP_descr = ''
# Owner Key: The key for enabling clients to own their data for entity correlation.
vvmmUsrAccP_ownerKey = ''
# Owner Tag: A tag for enabling clients to add their own data. For example, to indicate who created this object.
vmmUsrAccP_ownerTag = ''
# Alias: An alias for enabling clients to change the displayed name of an object in the APIC GUI.
vmmUsrAccP_nameAlias = ''
# User: The username for the VM provider account.
vmmUsrAccP_usr = 'administrator@vsphere.local'
# Configure policy:
vmmUsrAccP = cobra.model.vmm.UsrAccP(vmmDomP, annotation=vmmUsrAccP_annotation, descr=vmmUsrAccP_descr, name=vvmmUsrAccP_name, nameAlias=vmmUsrAccP_nameAlias, ownerKey=vvmmUsrAccP_ownerKey, ownerTag=vmmUsrAccP_ownerTag, usr=vmmUsrAccP_usr)

# Commit the generated code to APIC
print(toXMLStr(infraInfra))
c = cobra.mit.request.ConfigRequest()
c.addMo(infraInfra)
md.commit(c)

print(toXMLStr(polUni))
c = cobra.mit.request.ConfigRequest()
c.addMo(polUni)
md.commit(c)

print(toXMLStr(topMo))
c = cobra.mit.request.ConfigRequest()
c.addMo(topMo)
md.commit(c)