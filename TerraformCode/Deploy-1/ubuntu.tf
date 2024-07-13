resource "proxmox_vm_qemu" "UbuntuCloudInitVM" {
  name        = var.vm_name
  target_node = var.target_node
  clone       = var.clone
  full_clone  = true
  vmid        = var.vm_id

  agent       = 1
  os_type     = "cloud-init"
  cores       = var.cores
  sockets     = var.sockets
  cpu         = "host"
  memory      = var.memory
  scsihw      = "virtio-scsi-pci"
  bootdisk    = "scsi0"

  disk {
    slot    = 0
    size    = var.disk_size
    type    = "scsi"
    storage = "local-lvm"
  }

  network {
    model  = var.network_model
    bridge = var.network_bridge
    tag    = var.network_tag
  }

  ipconfig0 = var.network_config_type == "dhcp" ? "ip=dhcp" : "ip=${var.ip}/24,gw=${var.gw}"
  nameserver = var.nameserver

  sshkeys = var.ssh_key
}
