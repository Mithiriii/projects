using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Shoot : MonoBehaviour
{
    public GameObject projectilePrefab;
    private Vector3 offsetProjectile = new Vector3(1.2f, 0, 0);

    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            var projectile = GameObject.Instantiate(
                projectilePrefab,
                transform.position + offsetProjectile,
                projectilePrefab.transform.rotation);
        }
    }
}
