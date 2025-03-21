using AutoMapper;
using Contracts;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Hosting;
using Newtonsoft.Json;
using System.Collections.Generic;
using System.Net;
using System.Xml.Linq;
using TransmonAdvaita.Helper;
using TransmonAdvaita.Model;
using TransmonAdvaita.Model.DTOs;
using TransmonAdvaita.Services;

namespace TransmonAdvaita.Controllers
{
    [Route("api/[controller]/[action]")]
    [ApiController]
    [Authorize]
    public class AllocationPlanController : ControllerBase
    {
            private IRepositoryWrapperForAdvaita _repository;
            public readonly ILoggerManager _logger;
            private IMapper _mapper;

        public AllocationPlanController(IRepositoryWrapperForAdvaita repository, ILoggerManager logger, IMapper mapper)
        {
            _logger = logger;
            _repository = repository;
            _mapper = mapper;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllActiveAllocationPlan([FromQuery] PagingParameter pagingParameter, [FromQuery] SearchParams searchParams)
        {
            ServiceResponse<IEnumerable<AllocationPlanDto>> serviceResponse = new ServiceResponse<IEnumerable<AllocationPlanDto>>();

            try
            {
                var allocationPlanList = await _repository.AllocationPlanService.GetAllActiveAllocationPlan(pagingParameter, searchParams);
                var metadata = new
                {
                    allocationPlanList.TotalCount,
                    allocationPlanList.PageSize,
                    allocationPlanList.CurrentPage,
                    allocationPlanList.HasNext,
                    allocationPlanList.HasPrevious
                };

                Response.Headers.Add("X-Pagination", JsonConvert.SerializeObject(metadata));
                _logger.LogInfo("Returned all AllocationPlan()s");
                var result = _mapper.Map<IEnumerable<AllocationPlanDto>>(allocationPlanList);
                serviceResponse.Data = result;
                serviceResponse.Message = "Success";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Ok(serviceResponse);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
                serviceResponse.Data = null;
                serviceResponse.Message = "Inter server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }


        [HttpGet]
        public async Task<IActionResult> GetAllAllocationPlan([FromQuery] PagingParameter pagingParameter, [FromQuery] SearchParams searchParams)
        {
            ServiceResponse <IEnumerable<AllocationPlanDto>> serviceResponse = new ServiceResponse<IEnumerable<AllocationPlanDto>>();

            try
            {
                var allocationPlanList = await _repository.AllocationPlanService.GetAllAllocationPlan(pagingParameter, searchParams);
                var metadata = new
                {
                    allocationPlanList.TotalCount,
                    allocationPlanList.PageSize,
                    allocationPlanList.CurrentPage,
                    allocationPlanList.HasNext,
                    allocationPlanList.HasPrevious
                };

                Response.Headers.Add("X-Pagination", JsonConvert.SerializeObject(metadata));
                _logger.LogInfo($"Returned allocationPlan()s");
                var result = _mapper.Map < IEnumerable<AllocationPlanDto>>(allocationPlanList);
                serviceResponse.Data = result;
                serviceResponse.Message = "Success";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Ok(serviceResponse);
                }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
                serviceResponse.Data = null;
                serviceResponse.Message = "Inter server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }


        [HttpGet]
        public async Task<IActionResult> GetallocationPlanById(int allocationPlanId)
        {
            ServiceResponse<AllocationPlanDto> serviceResponse = new ServiceResponse<AllocationPlanDto>();

            try
            {
                var allocationPlanList = await _repository.AllocationPlanService.GetallocationPlanById(allocationPlanId);
                if (allocationPlanList == null)
                {
                    _logger.LogError($"allocationPlan with id: {allocationPlanId}, hasn't been found in db.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = $"allocationPlan with id: {allocationPlanId}, hasn't been found in db.";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.NotFound;
                    return NotFound(serviceResponse);
                }
                else
                {
                    _logger.LogInfo($"Returned allocationPlan with id:  {allocationPlanId}");
                    var result = _mapper.Map<AllocationPlanDto>(allocationPlanList);
                    serviceResponse.Data = result;
                    serviceResponse.Message = "Success";
                    serviceResponse.Success = true;
                    serviceResponse.StatusCode = HttpStatusCode.OK;
                    return Ok(serviceResponse);
                }
            }
            catch (Exception ex)
            {
                _logger.LogError($"Something went wrong inside GetallocationPlanById action: {ex.Message}");
                serviceResponse.Data = null;
                serviceResponse.Message = "Inter server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }

        [HttpGet]
        public async Task<IActionResult> GetallocationPlanByName(int subSubProcessId, string allocationName)
        {
            ServiceResponse<AllocationPlanDto> serviceResponse = new ServiceResponse<AllocationPlanDto>();

            try
            {
                var allocationPlanList = await _repository.AllocationPlanService.GetallocationPlanByName(  subSubProcessId , allocationName);
                if (allocationPlanList == null)
                {
                    _logger.LogError($"allocationPlan with id: {subSubProcessId},{allocationName}, hasn't been found in db.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = $"allocationPlan with id: {subSubProcessId},{allocationName}, hasn't been found in db.";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.NotFound;
                    return NotFound(serviceResponse);
                }
                else
                {
                    _logger.LogInfo($"Returned allocationPlan with id: {subSubProcessId}, {allocationName}");
                    var result = _mapper.Map<AllocationPlanDto>(allocationPlanList);
                    serviceResponse.Data = result;
                    serviceResponse.Message = "Success";
                    serviceResponse.Success = true;
                    serviceResponse.StatusCode = HttpStatusCode.OK;
                    return Ok(serviceResponse);
                }
            }
            catch (Exception ex)
            {
                _logger.LogError($"Something went wrong inside GetallocationPlanByName action: {ex.Message}");
                serviceResponse.Data = null;
                serviceResponse.Message = "Inter server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }

        [HttpPost]
        public async Task<IActionResult> CreateAllocationPlan([FromBody] AllocationPlanDtoPost allocationPlanDtoPost)
        {
            ServiceResponse<AllocationPlanDto> serviceResponse = new ServiceResponse<AllocationPlanDto>();

            try
            {
                if (allocationPlanDtoPost == null)
                {
                    _logger.LogError("AllocationPlan object sent from client is null.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = "AllocationPlan object is null";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.BadRequest;
                    return BadRequest(serviceResponse);
                }
                if (!ModelState.IsValid)
                {
                    _logger.LogError("Invalid AllocationPlan object sent from client.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = "Invalid model object";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.BadRequest;
                    return BadRequest(serviceResponse);
                }

                var AllocationMappingEntity = _mapper.Map<IEnumerable<AllocationPlanMapping>>(allocationPlanDtoPost.AllocationMappings);
                var AllocationPlanEntity = _mapper.Map<AllocationPlan>(allocationPlanDtoPost);
                AllocationPlanEntity.AllocationMappings = AllocationMappingEntity.ToList();
                await _repository.AllocationPlanService.CreateAllocation(AllocationPlanEntity);
                _repository.SaveAsync();

                serviceResponse.Data = null;
                serviceResponse.Message = "Successfully Created";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Created("GetaAllocationPlanById", serviceResponse);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Something went wrong inside CreateAllocationPlan action: {ex.Message}");
                serviceResponse.Data = null;
                serviceResponse.Message = "Internal server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }

        [HttpPut]
        public async Task<IActionResult> UpdateAllocationPlan(int allocationPlanId, [FromBody] AllocationPlanDtoUpdate AllocationPlanDtoUpdate)
        {
            ServiceResponse<AllocationPlanDto> serviceResponse = new ServiceResponse<AllocationPlanDto>();

            try
            {
                if (AllocationPlanDtoUpdate is null)
                {
                    _logger.LogError("AllocationPlan object sent from client is null.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = "Update AllocationPlan object is null";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.BadRequest;
                    return BadRequest(serviceResponse);
                }
                if (!ModelState.IsValid)
                {
                    _logger.LogError("Invalid AllocationPlan object sent from client.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = "Invalid model object";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.BadRequest;
                    return BadRequest(serviceResponse);
                }

                var allocationPlans = await _repository.AllocationPlanService.GetallocationPlanById(allocationPlanId);
                if (allocationPlans is null)
                {
                    _logger.LogError($"AllocationPlan with id: {allocationPlanId}, hasn't been found in db.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = "AllocationPlan with the given id hasn't been found in db.";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.NotFound;
                    return NotFound(serviceResponse);
                }
                var allocationPlanEntity = _mapper.Map<AllocationPlan>(AllocationPlanDtoUpdate);
                var allocationMappingEntity = _mapper.Map<List<AllocationPlanMapping>>(AllocationPlanDtoUpdate.AllocationMappings);
                allocationPlanEntity.AllocationMappings = allocationMappingEntity;

                string result = await _repository.AllocationPlanService.UpdateAllocation(allocationPlanEntity);
                _logger.LogInfo(result);
                _repository.SaveAsync();
                serviceResponse.Data = null;
                serviceResponse.Message = "Updated Successfully";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Ok(serviceResponse);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Something went wrong inside UpdateAllocationPlan action: {ex.Message}");
                serviceResponse.Data = null;
                serviceResponse.Message = "Internal server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }

        [HttpPut]
        public async Task<IActionResult> ActivateAllocationPlan(int allocationPlanId)
        {
            ServiceResponse<AllocationPlanDto> serviceResponse = new ServiceResponse<AllocationPlanDto>();

            try
            {
                if (allocationPlanId == 0)
                {
                    _logger.LogError($"AllocationPlan with id: {allocationPlanId}, hasn't been found in db.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = "AllocationPlan object is null";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.BadRequest;
                    return BadRequest(serviceResponse);
                }
                var allocationPlans = await _repository.AllocationPlanService.GetallocationPlanById(allocationPlanId);

                allocationPlans.IsActive = true;
                if (allocationPlans is null)
                {
                    _logger.LogError($"AllocationPlan with id: {allocationPlanId}, hasn't been found in db.");
                    return NotFound(serviceResponse);
                }
                string result = await _repository.AllocationPlanService.UpdateAllocation(allocationPlans);
                _logger.LogInfo(result);
                _repository.SaveAsync();
                serviceResponse.Data = null;
                serviceResponse.Message = "Activate Successfully";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Ok(serviceResponse);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Something went wrong inside ActivateAllocationPlan action: {ex.Message}");
                serviceResponse.Data = null;
                serviceResponse.Message = "Internal server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }

        [HttpPut]
        public async Task<IActionResult> DeactivateAllocationPlan(int allocationPlanId)
        {
            ServiceResponse<AllocationPlanDto> serviceResponse = new ServiceResponse<AllocationPlanDto>();

            try
            {
                //var allocationPlans = await _allocationPlanService.GetallocationPlanById(subSubProcessId, allocationPlanId);
               // if (allocationPlans is null)
               if (allocationPlanId  == 0)
                {
                    _logger.LogError($"AllocationPlan with id: {allocationPlanId}, hasn't been found in db.");
                    serviceResponse.Data = null;
                    serviceResponse.Message = "AllocationPlan object is null";
                    serviceResponse.Success = false;
                    serviceResponse.StatusCode = HttpStatusCode.BadRequest;
                    return BadRequest(serviceResponse);
                }
                var allocationPlans = await _repository.AllocationPlanService.GetallocationPlanById(allocationPlanId);

                allocationPlans.IsActive = false;
                if(allocationPlans is null)
                {
                    _logger.LogError($"AllocationPlan with id: {allocationPlanId}, hasn't been found in db.");
                    return NotFound(serviceResponse);
                }
                string result = await _repository.AllocationPlanService.UpdateAllocation(allocationPlans);
                _logger.LogInfo(result);
                _repository.SaveAsync();
                serviceResponse.Data = null;
                serviceResponse.Message = "De-activated Successfully";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Ok(serviceResponse);
            }
            catch (Exception ex)
            {
                _logger.LogError($"Something went wrong inside DeactivateAllocationPlan action: {ex.Message}");
                serviceResponse.Data = null;
                serviceResponse.Message = "Internal server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }


        [HttpGet]
        public async Task<IActionResult> GetaAllocationPlanIdNameList()
        {
            ServiceResponse<IEnumerable<AllocationPlanIdNameDto>> serviceResponse = new ServiceResponse<IEnumerable<AllocationPlanIdNameDto>>();
            try
            {
                var allocationPlanList = await _repository.AllocationPlanService.GetaAllocationPlanIdNameList();
                _logger.LogInfo("Returned all AllocationPlans()s");
                var result = _mapper.Map<IEnumerable<AllocationPlanIdNameDto>>(allocationPlanList);
                serviceResponse.Data = result;
                serviceResponse.Message = "Success";
                serviceResponse.Success = true;
                serviceResponse.StatusCode = HttpStatusCode.OK;
                return Ok(serviceResponse);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex.Message);
                serviceResponse.Data = null;
                serviceResponse.Message = "Inter server error";
                serviceResponse.Success = false;
                serviceResponse.StatusCode = HttpStatusCode.InternalServerError;
                return StatusCode(500, serviceResponse);
            }
        }

    }
}
